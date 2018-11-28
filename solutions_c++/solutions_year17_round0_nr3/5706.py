#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int t,n,k,y,z,pos;
    cin>>t;
    vector<int> v;
    int q=0;
    while(q++<t){
        v.clear();
        cin>>n>>k;

        v.push_back(1);
        for(int i=1;i<=n;i++){
            v.push_back(0);
        }
        v.push_back(1);

        while(k--){
            int templ, tempr;
            z = -1;
            y = -1;
            pos = -1;
            for(int i=0;i<n+2;i++){

                templ = tempr = 0;

                if(v[i] == 0){

                    int c=i-1;
                    while(v[c--] == 0){
                        templ++;
                    }
                    c=i+1;
                    while(v[c++] == 0){
                        tempr++;
                    }

                    if(min(templ,tempr) > z || (min(templ,tempr) == z && max(templ,tempr) > y)){
                        z = min(templ,tempr);
                        pos = i;
                        y = max(templ,tempr);
                    }
                }


            }
            v[pos] = 1;
        }
        cout<<"Case #"<<q<<": "<<y<<" "<<z<<endl;
    }
}

