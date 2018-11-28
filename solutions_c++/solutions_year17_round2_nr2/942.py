#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

struct Frequency {
	char c;
	unsigned n;
	Frequency():
		c('_'),
		n(0) {}
	Frequency(char c, unsigned n):
		c(c),
		n(n) {}
	bool operator<(const Frequency& f) const {
		return n<f.n;
	}
};

bool generate3(Frequency a, Frequency b, Frequency c, std::string& result) {
	unsigned num = a.n + b.n + c.n;
	std::vector<Frequency> fv;
	fv.push_back(a);
	fv.push_back(b);
	fv.push_back(c);
	std::sort(fv.begin(),fv.end());
	if (num>1 && fv[2].n>num/2) {
		return false;
	}
	if (num == 1) {
		result = std::string(1,fv[2].c);
	}
	result = std::string(num,fv[2].c);
	for (unsigned i=2*fv[2].n;i<result.size();i+=2) {
		if (fv[0].n == 0) {
			assert(0);
		}
		result[i]=fv[0].c;
		--fv[0].n;
	}
	for (unsigned i=1;i<result.size();i+=2) {
		if (fv[0].n == 0) {
			if (fv[1].n == 0) {
				assert(0);
			}
			result[i]=fv[1].c;
			--fv[1].n;
		} else {
			result[i]=fv[0].c;
			--fv[0].n;
		}
	}
	if (fv[0].n != 0 || fv[1].n != 0) {
		assert(0);
	}
	return true;
}

void substitute(char a, char b, unsigned n, std::string& result) {
	if (n==0) {
		return;
	}
	std::string s;
	while (n>0) {
		(s+=a)+=b;
		--n;
	}
	size_t p = result.find(a);
	if (p == std::string::npos) {
		assert(0);
	}
	result.insert(p,s);
}

void printStr(unsigned i, const std::string& str) {
	printf("Case #%u: %s\n",i+1,str.c_str());
}

void printImpossible(unsigned i) {
	printStr(i,"IMPOSSIBLE");
}

void complement(unsigned i, Frequency a, Frequency b) {
	std::string result;
	if (generate3(a,b,Frequency(),result)) {
		printStr(i,result);
	} else {
		printImpossible(i);
	}
}

int main(int argc, char **argv) {

    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {

    	unsigned N, R, O, Y, G, B, V;

        scanf("%u %u %u %u %u %u %u\n",&N,&R,&O,&Y,&G,&B,&V);

        if (V>0) {
        	if (V+Y==N) {
				complement(i,Frequency('V',V),Frequency('Y',Y));
				continue;
        	}
        	if (V>=Y) {
        		printImpossible(i);
        		continue;
        	}
        	Y-=V;
        }

        if (O>0) {
        	if (O+B==N) {
        		complement(i,Frequency('O',O),Frequency('B',B));
				continue;
        	}
        	if (O>=B) {
        		printImpossible(i);
        		continue;
        	}
        	B-=O;
        }

        if (G>0) {
        	if (G+R==N) {
        		complement(i,Frequency('G',G),Frequency('R',R));
				continue;
        	}
        	if (G>=R) {
        		printImpossible(i);
        		continue;
        	}
        	R-=G;
        }

        std::string result;
        if (!generate3(Frequency('R',R),Frequency('Y',Y),Frequency('B',B),result)) {
        	printImpossible(i);
        	continue;
        }

        substitute('Y','V',V,result);
        substitute('B','O',O,result);
        substitute('R','G',G,result);

        if (result.size() != N) {
        	assert(0);
        }

        printStr(i,result);
    }

    return 0;
}














