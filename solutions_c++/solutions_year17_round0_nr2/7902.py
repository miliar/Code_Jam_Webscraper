#include <bits/stdc++.h>

using namespace std;
#define F first
#define S second
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    string kelma;
    cin>>t;
    for(int j=1; j<=t ; j++){
        cin>>kelma;
        if(kelma.size()==1)cout<<"Case #"<<j<<": "<<kelma<<endl;
        else{
            for(int i=0 ; i<kelma.size()-1 ; i++ ){
                if(kelma[i]>kelma[i+1]){
                    for(i ; i>0 ; i--){
                        if(kelma[i]!=kelma[i-1])break;
                    }
                    kelma[i]=kelma[i]-1;
                    i++;
                    for(i ; i<kelma.size() ; i++)
                        kelma[i]='9';
                    break;
                }
            }
            int z=0;
            for(z ; z<kelma.size() ; z++)
                if(kelma[z]!='0')break;
            kelma.erase(0,z);
            cout<<"Case #"<<j<<": "<<kelma<<endl;
        }

    }
/*
 * 888887
 *
    987 -> 899
    543456
    499999

    31999
    29999
  */
    return 0;
}