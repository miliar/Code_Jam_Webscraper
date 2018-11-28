using namespace std;

#include<bits/stdc++.h>

#define ll long long

struct data{
    ll mini, maci, serial;
};

struct sata{
    ll base, serial;
};

bool compare(data a, data b)
{
    if(a.mini==b.mini)
        if(a.maci==b.maci) return a.serial<b.serial;
        else return a.maci>b.maci;
    else return a.mini>b.mini;
}

int main(void)
{
    ///ios::sync_with_stdio(false);
    ///cin.tie(NULL);
    ///cout.tie(NULL);

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    ll T, N, K;
    cin>>T;

    for(int iter=1; iter<=T; iter++){
        cin>>N>>K;
        ll counter = 0, pre = 0, nex, lim = 0, serial;
        vector<sata> v[2];
        vector<data> sorted;
        data temp;
        sata samp;
        samp.base = N;
        samp.serial = 0;
        v[pre].push_back(samp);

        while(counter<K){
            lim += v[pre].size();

            /**for(ll i=0; i<v[pre].size(); i++) cout<<v[pre][i].base<<" ";
            cout<<"\n";**/

            nex = (pre+1)%2;
            if(lim>=K){
                counter++;
                for(ll i=0; i<v[pre].size(); i++){
                    temp.maci = v[pre][i].base/2;
                    if(v[pre][i].base%2) temp.mini = v[pre][i].base/2;
                    else temp.mini = max(v[pre][i].base/2-1, 0ll);
                    temp.serial = v[pre][i].serial;
                    sorted.push_back(temp);
                }

                sort(sorted.begin(), sorted.end(), compare);

                /***cout<<"Counter : "<<counter<<" Sorted :\n";
                for(ll i=0; i<sorted.size(); i++) cout<<sorted[i].mini<<" "<<sorted[i].maci<<" "<<sorted[i].serial<<"\n";***/


                ll i = 0;
                while(counter<K){counter++, i++;}
                cout<<"Case #"<<iter<<": "<<sorted[i].maci<<" "<<sorted[i].mini<<"\n";
            }
            else{
                counter = lim;
                serial = 0;
                v[nex].clear();

                for(ll i=0; i<v[pre].size(); i++){
                    if(v[pre][i].base>2){
                        if(v[pre][i].base%2){
                            samp.base = v[pre][i].base/2;
                            samp.serial = ++serial;
                            v[nex].push_back(samp);
                        }
                        else{
                            samp.base = v[pre][i].base/2-1;
                            samp.serial = ++serial;
                            v[nex].push_back(samp);
                        }
                    }
                    if(v[pre][i].base>1){
                        samp.base = v[pre][i].base/2;
                        samp.serial = ++serial;
                        v[nex].push_back(samp);
                    }

                }
                pre = nex;
            }
        }
        //cout<<"Case #"<<iter<<": "<<output<<"\n";
    }

return 0;
}
