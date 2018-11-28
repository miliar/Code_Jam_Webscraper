#include <bitset>
#include <queue>
#include <string>
#include <iostream>
using namespace std;
struct State
{
    State(const bitset<1000>& iP, int iF, int iT):p(iP), from(iF), times(iT){}
    bitset<1000> p;
    int from;
    int times;
};

bitset<1000> pancake;
int testFlip(int size, int K)
{
    if(pancake.count() == 1000) return 0;
    State state(pancake, -1, 0);
    queue<State> theQ;
    theQ.push(state);
    while(!theQ.empty())
    {
        State currentP = theQ.front();
        theQ.pop();
        for(int i=0; i<size-K+1; ++i)
        {
            if(i == currentP.from) continue; // skip same flip
            bitset<1000> tryFlip = currentP.p;
            bool possibleTry = false;
            if(tryFlip[i] != 0) continue;
            for(int j=i; j<i+K; ++j)
            {                
                tryFlip.flip(j);
            }
            if(tryFlip.count()==1000) return currentP.times+1;
            theQ.push(State(tryFlip, i, currentP.times+1));
            break;
        }
    }
    return -1;
}
int main(int argc, char* argv)
{
    int T;
    cin >> T;
    for(int t=0; t<T; ++t)
    {
        string S;
        int K;
        cin >> S >> K;
        
        pancake.set();
        for(int i=0; i<S.length(); ++i)
        {
            if(S[i]=='+') pancake[i]=1;
            if(S[i]=='-') pancake[i]=0;
        }
        int result = testFlip(S.length(), K);
        cout << "Case #" << (t+1) << ": ";
        if(result == -1)
        {
            cout << " IMPOSSIBLE" << endl;
        }
        else
        {
            cout << result << endl;
        }
        
    }
    return 0;
}