#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <queue>
#include <map>
#define PI 3.14159265358979323846

using namespace std;

typedef struct {
    int s;
    int f;
    int p;
} Node;

bool sortfunc(const Node& a, const Node& b) {
    return a.s < b.s;
}

bool sortfunc2(int a, int b) {
    return a > b;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T=0;
    int n, ac, aj, a, b;
    Node node;
    vector<Node> v;
    vector<int> extraTimeCanGive[2];
    vector<int> extraTimeCannotGive[2];
    int totalTime[2];
    int totalCanGive[2];
    int totalCannotGive[2];
    int startingPlayer,endingPlayer;
    int changes, difference;
    
    scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
        scanf("%d%d",&ac,&aj);
        v.clear();
        extraTimeCanGive[0].clear();
        extraTimeCanGive[1].clear();
        extraTimeCannotGive[0].clear();
        extraTimeCannotGive[1].clear();
        for (int i=0;i<2;i++) {
            totalTime[i]=totalCanGive[i]=totalCannotGive[i] = 0;
        }
        changes = 0;
        startingPlayer=endingPlayer=0;
        
        for (int i=0;i<ac;i++) {
            scanf("%d%d",&a,&b);
            node.s = a;
            node.f = b;
            node.p = 0;
            v.push_back(node);
        }
        
        for (int i=0;i<aj;i++) {
            scanf("%d%d",&a,&b);
            node.s = a;
            node.f = b;
            node.p = 1;
            v.push_back(node);
        }
        
        sort(v.begin(),v.end(),sortfunc);
        
        startingPlayer = v[0].p;
        endingPlayer = v[v.size()-1].p;
        if (startingPlayer!=endingPlayer) {
            changes=1;
            extraTimeCanGive[startingPlayer].push_back(v[0].s+1440-v[v.size()-1].f);
            totalCanGive[startingPlayer] += extraTimeCanGive[startingPlayer].back();
            totalTime[startingPlayer] = v[0].f+1440-v[v.size()-1].f;
        } else {   
            changes=0;
            extraTimeCannotGive[startingPlayer].push_back(v[0].s+1440-v[v.size()-1].f);
            totalCannotGive[startingPlayer] += extraTimeCannotGive[startingPlayer].back();
            totalTime[startingPlayer] = v[0].f+1440-v[v.size()-1].f;
        }
        
        for (int i=1;i<v.size();i++) {
            if (v[i-1].p==v[i].p) {
                extraTimeCannotGive[v[i].p].push_back(v[i].s-v[i-1].f);
                totalCannotGive[v[i].p] += extraTimeCannotGive[v[i].p].back();
                totalTime[v[i].p] += v[i].f-v[i-1].f;
            } else {
                changes++;
                extraTimeCanGive[v[i].p].push_back(v[i].s-v[i-1].f);
                totalCanGive[v[i].p] += extraTimeCanGive[v[i].p].back();
                totalTime[v[i].p] += v[i].f-v[i-1].f;
            }
        }
        
        if (totalTime[0]>totalTime[1]) {
            if (720-totalTime[1] > totalCanGive[0]) {
                difference = 720-totalTime[1]-totalCanGive[0];
                
                sort(extraTimeCannotGive[0].begin(),extraTimeCannotGive[0].end(),sortfunc2);
                for (int i=0;i<extraTimeCannotGive[0].size();i++) {
                    difference -= extraTimeCannotGive[0][i];
                    changes+=2;
                    if (difference<=0) {
                        break;
                    }
                }
            }
        } else {
            if (totalTime[0]<totalTime[1]) {
                if (720-totalTime[0] > totalCanGive[1]) {
                    difference = 720-totalTime[0]-totalCanGive[1];
                    
                    sort(extraTimeCannotGive[1].begin(),extraTimeCannotGive[1].end(),sortfunc2);
                    for (int i=0;i<extraTimeCannotGive[1].size();i++) {
                        difference -= extraTimeCannotGive[1][i];
                        changes+=2;
                        if (difference<=0) {
                            break;
                        }
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n",t,changes);
    }
}