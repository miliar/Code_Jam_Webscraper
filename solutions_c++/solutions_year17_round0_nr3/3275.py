#include <iostream>
#include <vector>
#include <fstream>
#include <map>
using namespace std;

long long get_lower_power_of_2(int a) {
    long long power = 1;
    while((power * 2) <= a)
        power*=2;
    return power;

}

pair <long long, long long> integer_division(int a, int b) {
    return make_pair<long long, long long>(a/b, a%b);
}
pair <long long, long long> solve(long long N, long long K) {
    long long power_2_x_1 = get_lower_power_of_2(K) - 1;
   
    pair <long long, long long> partit = integer_division(N - power_2_x_1, power_2_x_1 + 1);
    if(partit.second >= K - power_2_x_1) {
        long long l = (partit.first) / 2;
        long long r = (partit.first) / 2 + (partit.first) % 2;
        return make_pair<long long, long long>(r, l);
    }
    else {
        long long l = (partit.first - 1) / 2;
        long long r = (partit.first - 1) / 2 + (partit.first - 1) % 2;
        return make_pair<long long, long long>(r, l);
    }

}
int main(int argc, char *argv[]) {    
	FILE *fin, *fout;
	if (argc > 1)
	{
		char tname[200];
		fin = fopen(argv[1],"r");
		strncpy (tname,argv[1],200);
		strncpy(strstr (tname,".in"),".out",4);
		fout = fopen(tname,"w");
	} else {
		fin = fopen("C-small-2-attempt0.in","r");
		fout = fopen("C.out","w");
	}


	int t;
	fscanf(fin,"%d",&t);

	for (int ti=0; ti<t; ti++)
	{
		long long n,k;
		fscanf(fin,"%lld", &n);
		fscanf(fin,"%lld", &k);
        pair<long long, long long> ans = solve(n,k);

		fprintf(fout,"Case #%d: %lld %lld\n", ti+1, ans.first, ans.second);

	}
	fclose(fin);
	fclose(fout);
}