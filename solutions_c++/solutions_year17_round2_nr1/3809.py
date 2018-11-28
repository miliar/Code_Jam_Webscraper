#include<bits/stdc++.h>
using namespace std;
int main (){
    int t;
    double d, n, k, s, time, big = 0.0, velocity;
	FILE *fin = freopen("A-large (1).IN", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("saanu_large.out", "w", stdout);
    cin>>t;
    for(int ii = 1; ii <= t; ii++){
        big = 0.0;
        cout<<"Case #"<<ii<<": ";
        cin>>d>>n;
        for(int i = 0; i < n; i++){
            cin>>k>>s;
            time = (d - k) / s;
            if(time > big){
                big = time;
            }
        }
        velocity = d / big;
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    std::cout << velocity<<endl;
    }
}
