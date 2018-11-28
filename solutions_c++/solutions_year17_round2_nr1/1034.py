#include <cstdio>



double maxFollowSpeed(unsigned long long D, unsigned long long K, unsigned long long S) {
	return (double)(S*D)/(double)(D-K);
}


int main(int argc, char **argv) {

    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {
        unsigned long long D, N;
        scanf("%llu %llu\n",&D,&N);

        unsigned long long K,S;
		scanf("%llu %llu\n",&K,&S);

		double cruiseSpeed = maxFollowSpeed(D,K,S);

        for (unsigned j=0;j<N-1;++j) {
        	scanf("%llu %llu\n",&K,&S);
        	double s = maxFollowSpeed(D,K,S);
        	if (s<cruiseSpeed) {
        		cruiseSpeed = s;
        	}
        }

        printf("Case #%u: %.8f\n",i+1,cruiseSpeed);
    }

    return 0;
}







