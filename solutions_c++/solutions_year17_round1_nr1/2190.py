#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class alphabetcake {
	private:
		int r, c;
		std::vector<std::string> cake;

		std::vector<std::vector<std::vector<std::vector<int> > > > memo;

		std::vector<std::string> sol;

		int recsol(unsigned rb, unsigned re, unsigned cb, unsigned ce) {
			if ((re - rb <= 0) || (ce - cb <= 0)) {
				return -1;
			}
			int csol = memo.at(rb).at(re).at(cb).at(ce);
			if (csol != 0) {
				return csol;
			}
			std::string lf = findinitials(rb, re, cb, ce);
			if (lf.size() == 0) {
				csol = -1;
			} else if (lf.size() == 1) {
				csol = 1;
			} else {
				for (unsigned i = rb + 1; (csol == 0) && (i < re); ++i) {
					if ((recsol(rb, i, cb, ce) != -1) && (recsol(i, re, cb, ce) != -1)) {
						csol = static_cast<int>(i) + 2;
					}
				}
				for (unsigned j = cb + 1; (csol == 0) && (j < ce); ++j) {
					if ((recsol(rb, re, cb, j) != -1) && (recsol(rb, re, j, ce) != -1)) {
						csol = -(static_cast<int>(j) + 2);
					}
				}
				if (csol == 0) {
					csol = -1;
				}
			}
			if (csol == 0) {
				throw "fail csol == 0";
			}
			memo.at(rb).at(re).at(cb).at(ce) = csol;
			return csol;
		}

		void reconstruct(unsigned rb, unsigned re, unsigned cb, unsigned ce) {
			int csol = memo.at(rb).at(re).at(cb).at(ce);
			if (csol == 0) {
				throw "fail csol == 0";
			} else if (csol == -1) {
				throw "fail no subsolution";
			} else if (csol == 1) {
				std::string lf = findinitials(rb, re, cb, ce);
				if (lf.size() != 1) {
					throw "fail not exactly one initial";
				}
				for (unsigned i = rb; i < re; ++i) {
					for (unsigned j = cb; j < ce; ++j) {
						sol.at(i).at(j) = lf.at(0);
					}
				}
			} else if (csol > 1) {
				reconstruct(rb, csol - 2, cb, ce);
				reconstruct(csol - 2, re, cb, ce);
			} else /* csol < -1 */ {
				reconstruct(rb, re, cb, -(csol + 2));
				reconstruct(rb, re, -(csol + 2), ce);
			}
		}

		const std::string findinitials(unsigned rb, unsigned re, unsigned cb, unsigned ce) {
			std::string lf;
			for (unsigned i = rb; i < re; ++i) {
				for (unsigned j = cb; j < ce; ++j) {
					if (cake.at(i).at(j) != '?') {
						lf += cake.at(i).at(j);
					}
				}
			}
			return lf;
		}

	public:
		void input(std::istream &is) {
			is >> r >> c;
			cake.reserve(r);
			std::string row;
			for (int i = 0; i < r; ++i) {
				is >> row;
				cake.push_back(row);
			}
		}

		void solve() {
			memo.resize(cake.size() + 1, std::vector<std::vector<std::vector<int> > >(cake.size() + 1, std::vector<std::vector<int> >(cake.at(0).size() + 1, std::vector<int>(cake.at(0).size() + 1, 0))));
			int csol = recsol(0, cake.size(), 0, cake.at(0).size());
			if (csol == -1) {
				throw "fail no solution found";
			}
			sol = cake;
			reconstruct(0, cake.size(), 0, cake.at(0).size());
		}

		void output(std::ostream &os) {
			for (std::vector<std::string>::const_iterator si = sol.begin(); si < sol.end(); ++si) {
				os << std::endl << (*si);
			}
		}
};

int main(void) {
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		alphabetcake task;
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
