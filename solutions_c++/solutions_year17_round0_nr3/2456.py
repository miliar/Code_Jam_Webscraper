#include <cstdio>


unsigned long long maxMinDistance(unsigned long long room) {
	return room/2;
}

unsigned long long minMinDistance(unsigned long long room) {
	if (room%2 == 0) {
	    return room/2-1;
	}
	return room/2;
}

unsigned long long mexLePow2(unsigned long long K) {
    unsigned long long p2 = 1;
    while (p2<=K) {
        p2*=2;
    }
    return p2/2;
}

unsigned long long getUserRoom(unsigned long long N, unsigned long long K) {
    unsigned long long p2 = mexLePow2(K);
    unsigned long long k = K-p2;
    unsigned long long z = (N-(p2-1))/p2;
    unsigned long long m = (N-(p2-1))%p2;
    if (k<m) {
        return z+1;
    }
    return z;
}

int main(int argc, char **argv) {

    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {
        unsigned long long N, K;

        scanf("%llu %llu\n",&N,&K);

        unsigned long long room = getUserRoom(N,K);

        printf("Case #%u: %llu %llu\n",i+1,maxMinDistance(room),minMinDistance(room));
    }

    return 0;
}







