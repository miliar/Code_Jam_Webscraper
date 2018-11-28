#include <bits/stdc++.h>

#define lp(i,n) for(long long int i=0; i<n; i++)

#define ll long long
#define pb push_back
#define  mp make_pair
#define pii pair<int,int>
#define ff first
#define ss second
#define nl "\n"

#define EPS 1e-8
#define OO 10000000

#define on(i,n) i=i|(1<<n)
#define off(i,n) i=i& (~(1<<n))

using namespace std;

bool check (string s){

    lp(i,s.size()){
        if(s[i]=='-') return false;
    }
    return true;


}

string turn(string s, int idx, int k){

    for(int i=0; i<k; i++){
        if(s[idx+i]=='-')s[idx+i]='+';
        else{s[idx+i]='-';}


    }
    return s;

}

int bfs(string s,int k){

    queue<string> q;
    q.push(s);
    map<string,int> my_map;
    my_map[s]=0;

    while(!q.empty()){
        string curr=q.front();
        q.pop();

        if(check(curr)) return my_map[curr];


        lp(i,s.size()-k+1){
                string nw=turn(curr,i,k);
                if(my_map.count(nw)==0){
                    my_map[nw]=my_map[curr]+1;
                     q.push(nw);

                }


        }






    }
    return -1;





}


int main(){
     freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);

   int t;
   cin>>t;
   int cs=1;
   while(t--){
            string s;
           cin>>s;
           int k;
           cin>>k;
            int ans=bfs(s,k);



            printf("Case #%d: ",cs++);

            if(ans==-1) cout<<"IMPOSSIBLE\n";
            else cout<<ans<<endl;

   }


}
