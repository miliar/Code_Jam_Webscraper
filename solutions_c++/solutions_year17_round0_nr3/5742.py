#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

typedef long long int lli;


struct Stall{

    lli LS,RS, S;
    bool is_empty;

    bool operator<( const Stall& other ) const
    {
            auto min_current = min(this->LS, this->RS);
            auto min_other = min(other.LS, other.RS);

            if(min_current != min_other){

                return min_current > min_other;

            }


            auto max_current = max(this->LS, this->RS);
            auto max_other = max(other.LS, other.RS);

            if(max_current != max_other){

                return max_current > max_other;

            }

            return this->S < other.S;

    }

};

struct LRS{

    lli y;
    lli z;

};

LRS solve_brute_force(lli N, lli K){

    LRS ans;

    set<Stall> bathroom;
    vector<Stall> stalls;

    for(lli i=0; i<N; i++){

        Stall s;
        s.LS = i;
        s.RS = N-i-1;
        s.S = i;
        s.is_empty = true;
        bathroom.insert(s);
        stalls.push_back(s);
    }


    for(lli i=1; i<=K; i++){

        auto it = bathroom.begin();
        auto s = *it;
        bathroom.erase(it);

        stalls[s.S].is_empty = false;

        if(i == K){

            ans.y = max(s.LS, s.RS);
            ans.z = min(s.LS, s.RS);
            break;
        }

        for(int direction=-1; direction<=1; direction+=2){

            lli current_idx = s.S + direction;

            while(current_idx >= 0 && current_idx < N && stalls[current_idx].is_empty){

                auto it1 = bathroom.find(stalls[current_idx]);
                bathroom.erase(it1);

                if(direction == -1){

                    stalls[current_idx].RS = s.S-current_idx-1;
                } else {

                    stalls[current_idx].LS = current_idx-s.S-1;
                }

                bathroom.insert(stalls[current_idx]);

                current_idx += direction;


            }

        }


    }

    return ans;


}

int main(int argc, char *argv[])
{
    int T;
    cin>>T;

    lli N,K;

    for(int c=1; c<=T; c++){

        cin>>N>>K;

        LRS ans = solve_brute_force(N, K);

        cout<<"Case #"<<c<<": "<<ans.y<<" "<<ans.z<<endl;

    }
    return 0;
}
