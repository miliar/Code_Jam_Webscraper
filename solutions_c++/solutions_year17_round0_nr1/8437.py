
#include <iostream>
#include <string>
#include <bitset>
#include <set>
#include <queue>
#include <utility>

using namespace std;

string initPancakeState;
int flipSize;

struct Comparer {
    bool operator() (const bitset<1000> &b1, const bitset<1000> &b2 ) const {
        return b1.to_ulong() < b2.to_ulong();
    }
};


set< bitset<1000>, Comparer> pancakeStateSet;
bitset<1000> initPancakeBit;
int numPancake;

bool isPossible = false;
int minFlipCount = 0;


void bfs() {
    if ( initPancakeBit.count() == numPancake ) {
        isPossible = true;
        minFlipCount = 0;
    }
    
    queue< pair<bitset<1000>, int> > openPancake;
    pancakeStateSet.insert( initPancakeBit );
    openPancake.push( make_pair(initPancakeBit, 0) );
    
    while ( !openPancake.empty() ) {
        if ( isPossible )
            break;
        
        bitset<1000> currState = openPancake.front().first;
        int currFlipCount = openPancake.front().second;
        openPancake.pop();
        
        for ( int i = 0; i <= numPancake - flipSize; ++i ) {
            bitset<1000> nextState ( currState );
            for ( int j = 0; j < flipSize; ++j )
                nextState.flip ( i + j );
            
            if ( pancakeStateSet.find( nextState ) != pancakeStateSet.end() )
                continue;
            
            int nextFlipCount = currFlipCount + 1;
            
            if ( nextState.count() == numPancake ) {
                minFlipCount = nextFlipCount;
                isPossible = true;
                break;
            }
            
            openPancake.push( make_pair( nextState, nextFlipCount ) );
            pancakeStateSet.insert( nextState );
        }
    }
}

int main()
{
freopen("/Users/kuk/Documents/studio/GCJ/GCJ/in.txt", "r", stdin);
freopen("/Users/kuk/Documents/studio/GCJ/GCJ/out.txt", "w", stdout);
    
    int T; cin >> T;
    
    int caseNo = 0;
    while ( T-- > 0 ) {
        caseNo++;
        
        cin >> initPancakeState >> flipSize;
        pancakeStateSet.clear();
        isPossible = false;
        minFlipCount = 0;
        initPancakeBit.reset();
        numPancake = (int)initPancakeState.length();
        
        for ( int i = 0; i< initPancakeState.length(); ++i )
            if ( initPancakeState[i] == '+' )
                initPancakeBit.set( i, true );
        
        bfs();
        
        printf("Case #%d: ", caseNo);
        if ( !isPossible )
            printf("IMPOSSIBLE");
        else
            printf("%d", minFlipCount);
        printf("\n");
    }
    return 0;
}
