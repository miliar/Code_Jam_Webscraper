#include<bits/stdc++.h>
#include<fstream>
using namespace std;

int main(){
    long long int t;
    ifstream f ;
    f.open("B-large.in");
    ofstream out ;
    out.open("out.txt");
    f >> t;
    long long int a=1;
    while(a<=t){
        long long int n,rem,i,pos=-1;
        f >> n;
        vector<long long int> v;
        while(n>0){
            rem = n%10;
            n = n/10;
            v.push_back(rem);
        }
        long long int len = v.size();
        for(i=len-1;i>0;i--){
            if(v[i]>v[i-1]){
                pos = i-1;
                v[i]--;
                if(i+1<len && v[i+1]>v[i]){
                    i+=2;
                }
                else{
                    for(long long int y=pos; y>=0; y--){
                        v[y]=9;
                    }
                    break;
                }
            }
        }
        long long int ans=0;
        for(i=len-1; i>=0; i--){
            ans = ans*10 + v[i];
        }
        out << "Case #" << a << ": ";
        out << ans << endl;
        a++;
    }
    f.close();
    out.close();
}
