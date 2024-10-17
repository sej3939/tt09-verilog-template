# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Test project behavior")

    # Set the input values you want to test


    addends = [i for i in range(-32,32)]

    for i in range(64):
        dut.a.value = addends[i] % 16
        for j in range(64):
            dut.b.value = addends[j] % 16

            # Wait for one clock cycle to see the output values
            await ClockCycles(dut.clk, 10)

            # The following assersion is just an example of how to check the output values.
            # Change it to match the actual expected output of your module:
            dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
            # If these passes don't work, fail the program and show what you failed.
            assert dut.sum.value == ((addends[i] + addends[j]) % 16) and dut.carry_out.value == ((addends[i] % 16 + addends[j] % 16) >= 16)
    
            # Keep testing the module by changing the input values, waiting for
            # one or more clock cycles, and asserting the expected output values.
        
