#include <iostream>
#include <fstream>
#include <ostream>
#include <vector>
#include <sstream>
#include <unordered_set>

using namespace std;



#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

typedef vector<vector<char>> vv;
int postion(int a, int b, int m){
    return a*m+b;
}
//
//pair<int,int> getpos(int p, int m){
//    return make_pair(p/m, p%m);
//}

//bool isright(vv& h){
//    unordered_set<int> visited;
//    for(int i=0;i<h.size();i++){
//        for(int j=0;j<h[0].size();j++){
//            int pos=postion(i,j,h.size());
//            if(!visited.count(pos)){
//                visited.insert(pos);
//            }
//        }
//    }
//}
//
//vv dfs(vv& h, unordered_set<char> us){
//    if(isright(h)) return h;
//    for(auto& a:h){
//        for(auto& b:a){
//            if(b=='?'){
//                
//            }
//        }
//    }
//}

vector<vector<char>> helper(vector<vector<char>>& h){
    vv res;
    //unordered_set<char> us;
    //unordered_set<int> pos;
    //int m=h.size();
    for(int i=0;i<h.size();i++){
        for(int j=0;j<h[0].size();j++){
            if(h[i][j]!='?'){
                //us.insert(h[i][j]);
                int z=j-1;
                while(z>=0 && h[i][z]=='?')  h[i][z--]=h[i][j];
                z=j+1;
                while(z<h[i].size() && h[i][z]=='?')  h[i][z++]=h[i][j];
            }
        }
    }
    
    for(int i=0;i<h.size();i++){
        if(h[i][0]=='?'){
            int j=i;
            while(j>=0 && h[j][0]=='?'){
                j--;
            }
            if(j<0){
                j=i;
                while(j<h.size() && h[j][0]=='?') j++;
            }
            vector<char> temp=h[j];
            h[i]=temp;
        }
    }
    //int emptysize=pos.size();
    //if(us.size()==0) return h;
    //vector<char> v(us.begin(),us.end());
//    int totalletter=us.size();
    //int num=0;
    //cout<<us.size()<<endl;
//    if(v.size()==0) return h;
    //int total=v.size();
//    for(int i=0;i<h.size();i++){
//        for(int j=0;j<h[0].size();j++){
//            if(h[i][j]=='?'){
//                if(i==0 && j==0){
//                    
//                }
////                h[i][j]=v[num%total];
////                num++;
//                h[i][j]=a;
//            }
//        }
//    }
    return h;
}

int main(){
    ifstream f("small.txt");
    ofstream myfile("output.txt");
    int N;
    f>>N;
    rep2(nn,1,N+1) {
        //string str;
        long long int n,k;
        f>>n>>k;
        vv res;
        for(int i=0;i<n;i++){
            string s;
            f>>s;
            vector<char> v;
            for(int j=0;j<k;j++){
                v.push_back(s[j]);
            }
            res.push_back(v);
        }
        vv ans=helper(res);
        myfile << "Case #"<<nn<<": "<<endl;
        for(int i=0;i<ans.size();i++){
            for(int j=0;j<ans[0].size();j++){
                myfile<<ans[i][j];
            }
            myfile<<endl;
        }
    }
    myfile.close();
    
    return 0;
}




