#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <iomanip>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

void output(vector<int> res2, vector<int> counts_back) {
    vector<int> counts(6, 0);
    for(auto& x : res2) {
        char lookup[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
        cout << lookup[x];
        counts[x]++;
    }
    /*rep(i, 6) {
        cout << counts[i] << " " << counts_back[i] << " | ";
    }
    */
    //cout << endl;
    assert(counts == counts_back);
}


vector<int> solveEasy(vector<int> counts) {
    int n=0;
    for(auto& x : counts) {
        n += x;
    } 

    vector<pair<int,int> > counts2;
    rep(i, 3) {
        counts2.push_back(make_pair(counts[i], i));
    }

    sort(counts2.begin(), counts2.end());

    int a = counts2[2].first;
    int b = counts2[1].first;
    int c = counts2[0].first;

    int aa = counts2[2].second;
    int bb = counts2[1].second;
    int cc = counts2[0].second;

    vector<int> fail;

    vector<int> res;

    rep(i, a) {
        res.push_back(aa);
        if(b == 0 && c == 0) {
            return fail;
        }
        if(b > c) {
            res.push_back(bb);
            b--;
        } else {
            res.push_back(cc);
            c--;
        }

        if(i == a-1) {
            bool delta = true;
            while(delta) {
                delta = false;
                if(b > 0 && bb != res[res.size()-1]) {
                    b--;
                    res.push_back(bb);
                    delta = true;
                }
                if(c > 0 && cc != res[res.size()-1]) {
                    c--;
                    res.push_back(cc);
                    delta = true;
                }
            }
        }
    }

    if(b != 0 || c != 0) {
        return fail;
    } else {
        return res;
    }
}

int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        int n; cin>>n;

        //r o y g b v
        vector<int> counts(6);
        rep(i, 6) {
            cin >> counts[i];
            //cout << counts[i] << " ";
        }
        //cout << endl;

        vector<int> counts_back = counts;

        vector<int> singles;
        vector<int> empties;

        bool fail = false;
        pair<int, int> links[3] = {{1, 4}, {3, 0}, {5, 2}}; //composite, opposite singule
        for(auto& x : links) {
            if(counts[x.second] > counts[x.first]) {
                counts[x.second] -= counts[x.first];
            } else if(counts[x.second] == counts[x.first]) {
                if(counts[x.second] == 0) {
                    empties.push_back(x.second);
                } else {
                    singles.push_back(x.second);
                }
            } else {
                fail = true;
            }
        }

        vector<int> anti_links(6, -1);
        for(auto& x : links) {
            anti_links[x.second] = x.first;
        }

        vector<int> res;

        int convert[3] = {0, 2, 4};

        if(fail) {
            cout << "IMPOSSIBLE";
        } else if(singles.size()) {
            if(singles.size() > 1 || empties.size() != 2) {
                cout << "IMPOSSIBLE";
            } else {
                vector<int> res2;
                rep(i, counts[singles[0]]) {
                    res2.push_back(singles[0]);
                    res2.push_back(anti_links[singles[0]]);
                }
                output(res2, counts_back);
            }
        } else {
            vector<int> easy;
            rep(i, 3) {
                easy.push_back(counts[convert[i]]);
            }
            vector<int> res = solveEasy(easy);


            if(res.size() == 0) {
                cout << "IMPOSSIBLE";
            } else {
                bool done[3] = {false, false, false};
                vector<int> res2;
                for(auto& x : res) {
                    int cur = convert[x];
                    res2.push_back(cur);
                    if(!done[x]) {
                        int alt = anti_links[cur];
                        assert(alt != -1);
                        rep(i, counts[alt]) {
                            res2.push_back(alt);
                            res2.push_back(cur);
                        }
                        done[x] = true;
                    }
                }

                output(res2,counts_back); 
            }
        }

        cout << endl;


    }
}
