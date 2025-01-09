#!/usr/bin/env python3

from xdsl.interpreter import Interpreter
from xdsl.tools.xdsl_run import xDSLRunMain

from xdsl_webgpu.interpreters.wgpu import WGPUFunctions


class xDSLWebGPURunMain(xDSLRunMain):
    def register_implementations(self, interpreter: Interpreter):
        super().register_implementations(interpreter)
        interpreter.register_implementations(WGPUFunctions())


def main():
    return xDSLWebGPURunMain().run()


if __name__ == "__main__":
    main()
