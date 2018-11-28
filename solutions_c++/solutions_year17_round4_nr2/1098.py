#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>

///////////////////////

using namespace std;

//Typedef
typedef long long int ll;

typedef map<ll, ll>  adjType;
typedef vector<map<ll, ll> > adjListType;
typedef vector<ll> pathSequenceType;
typedef pair<ll, pathSequenceType > pathType; 


//Global variable
ll startNode, endNode;
ll numNode;

const ll MAX_FLOW = 1000000000;

//Function definition
ll llMin(ll a, ll b);
ll llMax(ll a, ll b);

pathType getMaxPath(adjListType& adjList);
void updateAdjList(adjListType& adjList, pathSequenceType& pathSequence, ll pathFlow);
ll getMaxFlow(adjListType& adjList);



//Function declaration
ll llMin(ll a, ll b){ return a > b ? b : a; }
ll llMax(ll a, ll b){ return a > b ? a : b; }

pathType getMaxPath(adjListType& adjList){
    //Do djikstra algorithm while try to maximizing the flow and track the previous node which is optimal
    vector<ll> prevNode(numNode+1);
    vector<ll> hasChosen(numNode+1);
    vector<ll> maxFlow(numNode+1,-1);
    maxFlow[startNode] = MAX_FLOW;
    ll curNode = startNode;

    //std::cout << maxFlow.size() << std::endl;
    //Find the max flow path from start to end node
    while (curNode != endNode){
        // cout << "In getMaxPath while loop to find max flow with curNode: " << curNode << endl;
        hasChosen[curNode] = true;
        //Check all neighbour of curNode and update their maxFlow
        adjType& adj = adjList[curNode];
        for (adjType::iterator it = adj.begin(); it != adj.end(); ++it){
            ll adjNode = it->first;
            ll adjFlow = it->second;
            //std::cout << "curNode: " << curNode << ", Neighbour of node: " << adjNode << ", with flow:" << adjFlow << std::endl;
            if (!hasChosen[adjNode]){
                ll curFlow = llMin(maxFlow[curNode], adjFlow);
                if (curFlow > maxFlow[adjNode]){
                    maxFlow[adjNode] = curFlow;
                    prevNode[adjNode] = curNode;
                    //std::cout << "set maxFlow of adjNode: " << adjNode << std::endl;
                }
            }
        }
        //Get the new chosen node (the one with maxFlow but haven't been chosen)
        ll chosenNode = -1;
        ll chosenNodeMaxFlow = -1;
        for (ll node=0; node < maxFlow.size(); ++node){
            //std::cout << "node: " << node << ", maxFlow[node]: " << maxFlow[node] << std::endl;
            if (!hasChosen[node]){
                if (chosenNodeMaxFlow < maxFlow[node]){
                    chosenNode = node;
                    chosenNodeMaxFlow = maxFlow[node];
                }
            }
        }
        curNode = chosenNode;
        //std::cout << chosenNode << ", chosenNodeMaxFlow: " << chosenNodeMaxFlow << std::endl;
        if (chosenNodeMaxFlow <= 0) break;
    }

    //Generate the max flow path (trackback from the endnode)
    pathType result;
    if (maxFlow[endNode] <= 0) return result;

    result.first = maxFlow[endNode];
    curNode = endNode;
    result.second.push_back(curNode);
    //cout << "Before while loop to generate max flow path, curNode: " << curNode << endl;
    while (curNode != startNode){
        //cout << "In getMaxPath while loop to generate the max flow path with curNode: " << curNode << endl;
        curNode = prevNode[curNode];
        result.second.push_back(curNode);
    }
    //reverse the path (so that it start from startNode to endNode)
    reverse(result.second.begin(), result.second.end());

    //cout << "Finish get max path!" << endl;

    return result;
}

void updateAdjList(adjListType& adjList, pathSequenceType& pathSequence, ll pathFlow){
    for (ll i=0; i < pathSequence.size()-1; ++i){
        ll curNode = pathSequence[i], nextNode = pathSequence[i+1];
        //Reduce the capacity from curNode to nextNode by the value of pathFlow
        //But increase the capacity from the nextNode to curNode by the value of pathFlow
        adjList[curNode][nextNode] -= pathFlow;
        if (adjList[nextNode].find(curNode) != adjList[nextNode].end()) adjList[nextNode][curNode] += pathFlow;
        else adjList[nextNode][curNode] = pathFlow;
    }
}

ll getMaxFlow(adjListType& adjList){
    ll result = 0;
    bool canFindPath = true;
    //std::cout << "Start getMaxFlow with startNode: " << startNode << std::endl;
    while (canFindPath){
        pathType maxPath = getMaxPath(adjList);
        ll& pathFlow = maxPath.first;
        pathSequenceType& pathSequence = maxPath.second;
        if (pathFlow == 0){
            canFindPath = false;
            break;
        }
        result += pathFlow;
        updateAdjList(adjList, pathSequence, pathFlow);
        //cout << "In the while loop of getMaxFlow with pathFlow: " <<  pathFlow << endl;

    }
    return result;
}









///////////////////////


int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int N, C, M;
        std::cin >> N >> C >> M;
        std::vector<int> P(M), B(M);
        std::vector< std::vector<int> > cusPos(C, std::vector<int>(N, 0) );
        std::vector< std::vector<int> > numRemain(C, std::vector<int>(N, 0) );
        for (int i=0; i < M; ++i) {
            int PP, BB;
            std::cin >> PP >> BB;
            P[i] = PP-1;
            B[i] = BB-1;
            cusPos[BB-1][PP-1] += 1;
        }


        //For small case only
        //
        numNode = 4002;
        startNode = 4000; endNode = 4001;
        adjListType adjListDyn(numNode+1);
        for (ll i=0; i < N; ++i) {
            //Edge from source to first customer and between internal first customer
            if (cusPos[0][i] > 0) {
                adjListDyn[startNode][i] = 5000000;
                adjListDyn[i][i+1000] = cusPos[0][i];
            }
            //Edge from second customer to endNode and between internal second customer
            if (cusPos[1][i] > 0) {
                adjListDyn[i+3000][endNode] = 5000000;
                adjListDyn[i+2000][i+3000] = cusPos[1][i];
            }

            //Edge from first customer to the second customer (all except one with same position)
            if (cusPos[0][i] > 0) {
                for (ll j=0; j < N; ++j) {
                    if (i == j) continue;
                    if (cusPos[1][j] > 0) {
                        adjListDyn[i+1000][j+2000] = 5000000;
                    }
                }
            }
        }

        ll numFullNonPromotedRides = getMaxFlow(adjListDyn);
        // std::cout << numFullNonPromotedRides << std::endl;

        for (int i=0; i < N; ++i) {
            if (adjListDyn[i].find(i+1000) != adjListDyn[i].end()) {
                if (adjListDyn[i][i+1000] > 0) numRemain[0][i] = adjListDyn[i][i+1000];
            }
            if (adjListDyn[i+2000].find(i+3000) != adjListDyn[i+2000].end()) {
                if (adjListDyn[i+2000][i+3000] > 0) numRemain[1][i] = adjListDyn[i+2000][i+3000];
            }
        }

        ll numFullPromotedRides = 0;
        for (int i=1; i < N; ++i) {
            int minRide = numRemain[0][i] > numRemain[1][i] ? numRemain[1][i] : numRemain[0][i];
            numFullPromotedRides += minRide;
            numRemain[0][i] -= minRide;
            numRemain[1][i] -= minRide;
        }

        ll numSingleRides = 0;
        for (int i=0; i < N; ++i) {
            numSingleRides += numRemain[0][i] + numRemain[1][i];
        }

        std::cout << "Case #" << t << ": " << (numFullNonPromotedRides + numFullPromotedRides + numSingleRides) << " " << numFullPromotedRides << std::endl;


        



    }
    return 0;
}



