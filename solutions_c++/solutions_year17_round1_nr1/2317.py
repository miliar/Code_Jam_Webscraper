#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <cassert>

using namespace std;


struct LRS{

    bool is_possible;

    vector<string> A;
};


LRS is_possible(vector<string> A, int r, int c, char val, vector<set<int> >& pos_x, vector<set<int> >& pos_y){

    int idx = val - 'A';
    int i1_min = min(*pos_x[idx].begin(), r);
    int i1_max = max(*pos_x[idx].rbegin(), r);

    int j1_min = min(*pos_y[idx].begin(), c);
    int j1_max = max(*pos_y[idx].rbegin(), c);

    LRS rep;

    rep.A = A;

    //rep.A[r][c] = val;

    rep.is_possible = true;

    for(int i1=i1_min; i1<=i1_max; i1++){

        if(!rep.is_possible) break;

        for(int j1=j1_min; j1<= j1_max; j1++){

            if((rep.A[i1][j1] == '?') || (rep.A[i1][j1] == val)){

                rep.A[i1][j1] = val;


            } else {

                rep.is_possible = false;
                break;
            }


        }


    }

    if(rep.is_possible){

        pos_x[idx].insert(r);
        pos_y[idx].insert(c);

    }

    return rep;


}

vector<string> solve(vector<string> A){

    int R = A.size();
    int C = A[0].size();
    vector<string> ans = A;

    vector<set<int> > pos_x(26);
    vector<set<int> > pos_y(26);

    set<char> alphabet;


    // Fill force position

    for(int i=0; i<R; i++){

        for(int j=0; j<C; j++){

            if(A[i][j] != '?'){

                int idx = A[i][j]-'A';

                alphabet.insert(A[i][j]);

                pos_x[idx].insert(i);
                pos_y[idx].insert(j);

            }


        }
    }


    for(int i=0; i<26; i++){

        if(pos_x[i].size() > 0){

            for(int i1=*(pos_x[i].begin()); i1<=*(pos_x[i].rbegin()); i1++){


                for(int j1=*(pos_y[i].begin()); j1<=*(pos_y[i].rbegin()); j1++){

                    bool test = (ans[i1][j1] == '?') || (ans[i1][j1] == (i + 'A'));

                    assert(test);

                    ans[i1][j1] = (i + 'A');
                }
            }

        }

    }


    // Fill up remaining greedily

    for(int i=0; i<R; i++){

        for(int j=0; j<C; j++){

            if(ans[i][j] == '?'){

                for(auto val:alphabet){

                    auto response = is_possible(ans, i, j, val, pos_x, pos_y);

                    if(response.is_possible){

                        ans = response.A;

                        break;
                    }



                }

            }
        }
    }




    return ans;
}

int main(int argc, char *argv[])
{
    int T;
    cin>>T;

    int R,C;

    for(int c=1; c<=T; c++){

        cin>>R>>C;

        vector<string> A(R);

        for(int i=0; i<R; i++) cin>>A[i];

        vector<string> ans = solve(A);
        cout<<"Case #"<<c<<":"<<endl;

        for(int i=0; i<R; i++){
            cout<<ans[i]<<endl;
        }

    }
    return 0;
}
