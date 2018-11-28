#include <cstdio>
#include <vector>
#include <algorithm>

const static double PI = 3.14159265358979323846;

struct Pancake {
	Pancake(unsigned long long R, unsigned long long H):
		R(R), H(H) {}
	unsigned long long R;
	unsigned long long H;
	double side() const {
		return PI*2*H*R;
		//return PI*2*(double)(H*R);
		//return PI*2*(double)H*(double)R;
	}
	double top() const {
		return PI*R*R;
		//return PI*(double)R;
	}
};


struct PancakeCmpSide {
	bool operator()(const Pancake& p1,const Pancake& p2) {
		return p1.side()>p2.side();
	}
};

int main(int argc, char **argv) {
    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {

    	unsigned long long N,K;
		scanf("%llu %llu\n",&N,&K);

		std::vector<Pancake> pancakes;

		for (unsigned j=0;j<N;++j) {
			unsigned long long R,H;
			scanf("%llu %llu\n",&R,&H);
			pancakes.push_back(Pancake(R,H));
		}

		std::sort(pancakes.begin(),pancakes.end(),PancakeCmpSide());

		double maxExposedArea = 0;
		for (unsigned j=0;j<N;++j) {
			double exposedArea = pancakes[j].top() + pancakes[j].side();
			unsigned k = 1;
			unsigned kx = 0;
			while (k<K && kx<N) {
				if (kx!=j && pancakes[kx].R<=pancakes[j].R) {
					++k;
					exposedArea += pancakes[kx].side();
				}
				++kx;
			}
			if (k==K && exposedArea>maxExposedArea) {
				maxExposedArea = exposedArea;
			}
		}

        printf("Case #%u: %.9f\n",i+1,maxExposedArea);
    }

    return 0;
}


