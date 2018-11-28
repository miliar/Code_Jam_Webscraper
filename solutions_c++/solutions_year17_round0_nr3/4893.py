#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    ifstream infile;
    ofstream outfile;
	infile.open("C-small-2-attempt0.in");
    outfile.open("C-output.out");
    infile>>t;
    for(int tk=1;tk<=t;tk++){
        long long n,k;
        infile>>n>>k;
        long long x = 1;
        while(x*2+1 < k) x = x*2+1;
        k-=x;
        n-=x;
        x++;
        long long uv = ceil((double)n/(double)x);
        long long nov = uv*x - n;
        nov = x-nov;
        long long ans;
        if(k == 0) ans = n+1;
        else if(k <= nov) ans = uv;
        else ans = uv-1;
        // ans = uv or uv-1;
        outfile<<"Case #"<<tk<<": "<<ans/2<<" "<<ans - ans/2 - 1<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
