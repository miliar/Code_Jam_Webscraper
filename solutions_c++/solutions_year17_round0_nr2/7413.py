#include <iostream>
#include <string>

bool checkTidiness(long long n) {
	std::string ns;
	int nsl;
	ns = std::to_string(n);
	nsl = ns.length() - 1;

	for (int i = 0; i < nsl; ++i) {
		if(ns[i+1]<ns[i]) return false;
	}

	return true;
}

long long nextCandidate(long long n) {
	std::string ns;
	int nsl, nslminus;
	bool makenine = false;

	ns = std::to_string(n);
	nsl = ns.length() - 1;

	for (int i = 0; i < nsl; ++i) {
		if(makenine) {
			ns[i] = '9';
			continue;
		}
		if(ns[i+1]<ns[i]) {
			ns[i] = '0' + (std::stoi(ns.substr(i,1)) - 1);
			makenine = true;
		}
	}
	if (makenine) {
		ns[nsl] = '9';	
	}

	return std::stoll(ns);
}

long long maxTidy(long long n) {
	while (!checkTidiness(n)) {
		n = nextCandidate(n);
	}
	return n;
}

int main(int argc, char const *argv[]) {
	int t;
	long long n, result;
	std::cin >> t;
	for (int i = 0; i < t; ++i) {
		std::cin >> n;
		result = maxTidy(n);
		std::cout<<"Case #"<<i+1<<": "<<result<<std::endl;
	}
	return 0;
}