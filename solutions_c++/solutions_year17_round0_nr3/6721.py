#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

class Space
{
   public:
    int start;
    int end;

    Space(int start, int end)
    {
        this->start = start;
        this->end = end;
    }

    int val()
    {
        return end - start;
    }
};

pair<long long int, long long int> thinkOn(vector<Space> spaces, int enters)
{
    long long int x, y;

    while(enters != 0)
    {
        Space space = spaces.front();
        spaces.erase(spaces.begin());

        int pos = (space.start + space.end) / 2;
        x = space.end - pos;
        y = pos - space.start;

        if(space.start < pos){
            spaces.push_back(Space(space.start, pos - 1));
        }

        if(pos < space.end){
            spaces.push_back(Space(pos + 1, space.end));
        }

        sort(spaces.begin(), spaces.end(), [](Space& sp1, Space& sp2){
            if(sp1.val() > sp2.val())
                return true;
            else if(sp1.val() == sp2.val())
                return sp1.start < sp2.start;
            else
                return false;
        });
        --enters;
    }

    return {x, y};
}




int main(int argc, char *argv[])
{
    ifstream myCin;
    myCin.open("C-small-1-attempt0.in", ifstream::in);
    if (myCin.is_open()) {

        int T;
        myCin >> T;

        for(int i = 0; i < T; ++i)
        {
            long long int N, K;
            myCin >> N >> K;

            cout << "Case #" << (i + 1) << ": ";

            vector<Space> spaces(1, Space(0, N - 1));
            pair<long long int, long long int> result = thinkOn(spaces, K);
            cerr << result.first << " " << result.second << endl;
        }

    }
    myCin.close();
}
