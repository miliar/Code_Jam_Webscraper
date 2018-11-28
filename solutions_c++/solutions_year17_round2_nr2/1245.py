#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <iterator>
#include <fstream>
#include <cmath>
using namespace std;

bool notOk[100][100][100][3][3]={false};

char order[3]={0,1,2};


bool parcoursAlacon(int R, int Y, int B, int i, string &res) {
    if(res.size()==4) cerr<<res<<endl;
    int mini = min(R,min(Y,B));
    int maxi = max(R,max(Y,B));
    int one = 0, two = 0;
    if(i > 0) {
        if(res[0] == 'R') {
            if(R == maxi) one = 2;
            else if(R == mini) one = 0;
            else one = 1;
        }
        if(res[i-1] == 'R') {
            if(R == maxi) two = 2;
            else if(R == mini) two = 0;
            else two = 1;
        }
        if(res[0] == 'B') {
            if(B == maxi) one = 2;
            else if(B == mini) one = 0;
            else one = 1;
        }
        if(res[i-1] == 'B') {
            if(B == maxi) two = 2;
            else if(B == mini) two = 0;
            else two = 1;
        }
        if(res[0] == 'Y') {
            if(Y == maxi) one = 2;
            else if(Y == mini) one = 0;
            else one = 1;
        }
        if(res[i-1] == 'Y') {
            if(Y == maxi) two = 2;
            else if(Y == mini) two = 0;
            else two = 1;
        }
    }

    int mid = R+Y+B-maxi-mini;
    //if(maxi < 100 && notOk[mini][mid][maxi][one][two]) return false;

    if(i==res.size()) return true;
    if(R+Y+B!=1&&maxi> R+Y+B-maxi+(min(i,1))){
        return false;
    }

    if((i==0 || res[i-1] != 'R') && (i!=res.size()-1||res[0]!='R') && R) {
        res[i]='R';
        if(parcoursAlacon(R-1,Y,B,i+1,res)){
            return true;
        }
        res[i]='.';
    }

    if((i==0 || res[i-1] != 'Y') && (i!=res.size()-1||res[0]!='Y') && Y) {
        res[i]='Y';
        if(parcoursAlacon(R,Y-1,B,i+1,res)){
            return true;
        }
        res[i]='.';
    }
    if((i==0 || res[i-1] != 'B') && (i!=res.size()-1||res[0]!='B') && B) {
        res[i]='B';
        if(parcoursAlacon(R,Y,B-1,i+1,res)){
            return true;
        }
        res[i]='.';
    }
    return false;
}


int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out

    int T;
    cin>>T;
    for(int cas=1; cas<=T; cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int N,R,O,Y,G,B,V;
        cin>>N>>R>>O>>Y>>G>>B>>V;
        printf("%d %d %d %d ",N,R,Y,B);

        int maxi = max(R,max(Y,B));
        int mini = min(R,min(Y,B));

        vector<pair<int,char> > v;
        v.push_back(make_pair(R,'R'));
        v.push_back(make_pair(Y,'Y'));
        v.push_back(make_pair(B,'B'));

        sort(v.begin(),v.end());

        order[0] = v[0].second;
        order[1] = v[1].second;
        order[2] = v[2].second;


        string res=string(N,'.');
        if(parcoursAlacon(R,Y,B,0,res)) {
                cerr<<endl;
            cout<<res<<endl;
        } else {
            printf(" IMPOSSIBLE\n");
            cout<<"IMPOSSIBLE"<<endl;
        }
    }

}
