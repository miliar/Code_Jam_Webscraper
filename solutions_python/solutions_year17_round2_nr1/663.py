class Solution(object):
    base_folder = "/home/knut/Downloads/"
    out_folder = "results/"

    def __init__(self, name, test=False):
        self.test = test
        suffix = ".test" if test else ""
        self.input_file = self.base_folder + name + suffix + ".in"
        self.output_file = self.out_folder + name + suffix +  ".out"
        print("Reading")
        self.parse_input()
        print("Running")
        self.run()
        print("Writing")
        self.write_output()

    def run(self):
        pass

    def format_output(self):
        self.output_lines = ["Case #%s: %s" % (i+1, n)
                             for i, n in enumerate(self.results)]

    def parse_input(self):
        with open(self.input_file) as f:
            f.readline()
            self.inputs = [self.parse_line(line) for line in f.readlines()]

    def parse_line(self):
        pass

    def write_output(self):
        print("Writing to %s" % self.output_file)
        self.format_output()
        if self.test:
            return self.write_test()
        with open(self.output_file, "w") as f:
            f.write("\n".join(self.output_lines))

    def write_test(self):
        for line in self.output_lines:
            print(line)
