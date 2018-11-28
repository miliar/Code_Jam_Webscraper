#include <iostream>
#include <algorithm>
#include <climits>
#include <set>

using namespace std;
typedef   int ll;

const ll INF = LONG_LONG_MAX/2;
const bool dbg = false;

ll Ls,Rs;

struct cmpFreeSpace {

    bool operator() (const pair<ll,ll> & a, const pair<ll,ll> & b) const{
        if(a.first == b.first){
            return a.second < b.second;
        }

        return a.first  > b.first;
    }
};

struct cmpToiletPositon {

    bool operator() (const pair<ll,ll> & a, const pair<ll,ll> & b) const{
        if(a.first == b.first){
            return a.second > b.second;
        }

        return a.first  < b.first;
    }
};

pair<ll, ll> reversedPair(const  pair<ll, ll> & base){
    return make_pair(base.second, base.first);
};


//pair<position, distance to the right>
set<pair<ll,ll> ,cmpToiletPositon>toiletPositionSet;
//pair<distance to the right, position>
set<pair<ll,ll>, cmpFreeSpace> freeSpaceSet;

//guardians have ids: -1 and n

void simulateToiletTraffic(ll n, ll k){

    toiletPositionSet.insert(make_pair(-1, n));
    toiletPositionSet.insert(make_pair(n, -1));

    freeSpaceSet.insert(make_pair(n,-1));
    freeSpaceSet.insert(make_pair(-1,n));


    //start simulation
    for(ll visitorID = 0; visitorID < k; ++visitorID){
        auto bestToiletIt = freeSpaceSet.begin();


        //calculate position
        ll newPosition = (bestToiletIt->first +1) / 2  + bestToiletIt->second;


        //actualization
        pair<ll, ll> leftGuy = (*bestToiletIt);

        freeSpaceSet.erase(leftGuy);
        toiletPositionSet.erase(reversedPair(leftGuy));

        leftGuy.first = newPosition - leftGuy.second -1;
        Ls = leftGuy.first;

        freeSpaceSet.insert(leftGuy);
        toiletPositionSet.insert(reversedPair(leftGuy));

        //insert new guy to the toilet
        auto rightGuy = toiletPositionSet.upper_bound(make_pair(newPosition,1));


        ll newFreeSpace = rightGuy->first - newPosition -1;
        Rs = newFreeSpace;

        if(dbg)
            cout << "new guy " << newPosition << " " << newFreeSpace << endl;

        toiletPositionSet.insert(make_pair(newPosition, newFreeSpace));
        freeSpaceSet.insert(make_pair(newFreeSpace, newPosition));
    }
}

void printAnswer(){

    cout<< max(Ls, Rs) << " " << min(Ls, Rs);
}

void clearData(){
    toiletPositionSet.clear();
    freeSpaceSet.clear();
}

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    for(int caseId =1; caseId <=t; ++caseId){

         double  n,k;
        cin >> n >> k;

        if(n * 0.75  <= k){
            cout << "Case #" << caseId << ": 0 0\n";
            continue;
        }

        simulateToiletTraffic((int)n,(int)k);
        cout << "Case #" << caseId << ": ";
        printAnswer();
        cout << "\n";
        clearData();


    }

    return 0;
}