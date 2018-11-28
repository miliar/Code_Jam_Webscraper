#include <bits/stdc++.h>

using namespace std;

int n,k;
double u;
double p[60];

bool good(double x){
	double res = 0;
	for(int i =0 ; i<n; i++){
		if( p[i] < x){
			res += x - p[i];
		}
	}
	return res <= u;
}


int main(int argc, char *argv[])
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    //FILE *f = fopen("/home/quanganh/projects/TestQt/build-TestQt-Desktop-Debug/input.txt", "r");

    int num_test;
    //fscanf(f, "%d", &num_test);
    scanf("%d", &num_test);

    for (int test = 0; test < num_test; test++)
    {
    	scanf("%d %d", &n, &k);
    	scanf("%lf", &u);
    	
		for(int i=0; i<n; i++){
			scanf("%lf", &p[i]);		
		}
		double mn = 0, mx = 1;
		for(int i=0; i< 10000; i++){
			double mid = (mn + mx)/2;
			if( good(mid) ){
				mn = mid;
			}else{
				mx = mid;
			}
		}
		double res = 1.0f;
		for(int i=0; i<n; i++){
			res *=  max(p[i], mn);
		}
		

        printf("Case #%d: %0.8lf\n", test + 1, res);
    }

    return 0;
}

