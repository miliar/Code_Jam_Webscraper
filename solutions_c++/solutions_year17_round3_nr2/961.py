#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    freopen("B-small-attempt3.in.txt","r",stdin);
    freopen("smallout.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int ac,aj;
        cin >> ac >> aj;
        vector<pair<int,int> > cam,jam;
        for(int i = 0; i < ac; i++){
            int a,b;
            cin >> a >> b;
            cam.push_back(make_pair(a,b));
        }
        for(int i = 0; i < aj; i++){
            int a,b;
            cin >> a >> b;
            jam.push_back(make_pair(a,b));
        }
        if(ac + aj == 1){
            cout << "Case #" << t << ": 2\n";
        }
        else if(ac == 1 && aj == 1){
            cout << "Case #" << t << ": 2\n";
        }
        else{
            if(ac == 2){
                if((cam[1].first <= (cam[0].first+720)%1440 && (cam[0].first+720)%1440 < cam[1].second) || cam[0].first <= (cam[1].first+720)%1440 && (cam[1].first+720)%1440 < cam[0].second){
                    cout << "Case #" << t << ": 4\n";
                }
                else{
                    cout << "Case #" << t << ": 2\n";
                }
            }
            else{
                if((jam[1].first <= (jam[0].first+720)%1440 && (jam[0].first+720)%1440 < jam[1].second) || jam[0].first <= (jam[1].first+720)%1440 && (jam[1].first+720)%1440 < jam[0].second){
                    cout << "Case #" << t << ": 4\n";
                }
                else{
                    cout << "Case #" << t << ": 2\n";
                }
            }
        }
    }
    return 0;
}
