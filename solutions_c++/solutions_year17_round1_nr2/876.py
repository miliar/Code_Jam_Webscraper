#include <iostream>
#include <utility>
#include <cmath>
#include <vector>
#include <string>
using namespace std;
int n,p;

int main() {
    int t;
    cin >>t;
    for(int tt=1;tt<=t;tt++) {
        cin >> n >> p;
        vector<int> r;
        vector<vector<int>> q;
        vector<vector<pair<int,int>>> range;
        r.resize(n);
        for(int i=0;i<n;i++) {
            cin>>r[i];
        }

        q.resize(n);
        range.resize(n);
        for(int i=0;i<n;i++) {
            q[i].resize(p);
            range[i].resize(p);
            for(int j=0;j<p;j++) {
                cin>>q[i][j];

                double x = (double) q[i][j]/r[i];

                int up = ceil(x);
                int down = floor(x);
                
                while(true) {
                    if(q[i][j]>= (double) 0.9*up*r[i]) up++;
                    else {up--; break;}
                }

                while(true) {
                    if(q[i][j]<=(double) 1.1*down*r[i]) down--;
                    else {down++; break;}
                }

                range[i][j] = make_pair(down,up);
            }
            sort(range[i].begin(),range[i].end(),[](pair<int,int> p1, pair<int,int> p2) {
                    if(p1.first<p2.first) return true;
                    else if(p1.first>p2.first) return false;
                    else if(p1.second<p2.second) return true;
                    return false;
                    });
        }
        //for(int i=0;i<n;i++) {for(int j=0;j<p;j++) cout << "[" << range[i][j].first << ", " << range[i][j].second << "]"; cout << "\n";}

        cout << "Case #" << tt << ": ";
        vector<int> pos;
        pos.resize(n,0);
        int maxi=0;
        
        while(true) {
            int mini=0;
            int first=0, second=INT_MAX;
            for(int i=0;i<n;i++) {
                if(range[i][pos[i]].first<range[mini][pos[mini]].first) mini=i;
                else if(range[i][pos[i]].first<=range[mini][pos[mini]].first and range[i][pos[i]].second<range[mini][pos[mini]].second) mini=i;

                first = max(first, range[i][pos[i]].first);
                second = min(second, range[i][pos[i]].second);
            }

            
            if(first<=second) {
                maxi++;
                bool dobreak=false;
                for(int i=0;i<n;i++) {
                    pos[i]++;
                    if(pos[i]>=p) {dobreak = true; break;}
                }
                if(dobreak) break;
            }
            else {
                pos[mini]++;
                if(pos[mini]>=p) break;
            }
        }

        //if(n==1) {
        //    for(int j=0;j<p;j++) {
        //        if(range[0][j].first<=range[0][j].second) maxi++;
        //    }
        //}
        //else if(n==2) {
        //    int pos0=0;
        //    vector<bool> booked;
        //    booked.resize(p,false);
        //    while(pos0<p) {
        //        for(int j=0;j<p;j++) {
        //            if(max(range[0][pos0].first, range[1][j].first)<=min(range[0][pos0].second, range[1][j].second) and !booked[j]) {
        //                maxi++;
        //                booked[j]=true;
        //                break;
        //            }
        //        }
        //        pos0++;
        //    }
        //}
        cout << maxi << endl;

    }
    return 0;
}

