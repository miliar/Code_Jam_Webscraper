#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;
typedef long long ll;

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        ll n; infile>>n;
        vector<int> v;
        while (n>0){
            int d=n%10;
            v.push_back(d);
            n=(n-d)/10;
        }
        reverse(v.begin(),v.end());
        int z=v.size();
        int flag=-1;
        for (int i=0; i<z-1; i++){
            if (v[i]>v[i+1]){
                flag=i;
                break;
            }
        }
        int change=flag+1;
        if (flag>-1){
            while (change>0){
                if (v[change]<v[change-1]){
                    change--;
                    v[change]--;
                }
                else {
                    break;
                }
            }
        }
        //cout<<h<<" "<<change<<endl;
        if (flag>-1){
            for (int i=change+1; i<z; i++){
                v[i]=9;
            }
        }
        for (int i=0; i<z; i++){
            if ((i>0) || (v[i]!=0)){
                outfile<<v[i];
            }
        }
        outfile<<endl;
    }

}









