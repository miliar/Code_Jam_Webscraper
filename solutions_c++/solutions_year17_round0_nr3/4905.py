#include<bits/stdc++.h>
using namespace std;
void printoutput(int testcase,int ans1,int ans2){
    cout<<"Case #"<<testcase<<": "<<ans1<<" "<<ans2<<"\n";
    return;
}
priority_queue<int>q;
int main(){
    freopen("C:\\Users\\Dell\\Desktop\\inp.in", "r", stdin);
	freopen("C:\\Users\\Dell\\Desktop\\output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int testcase = 1; testcase <= t; testcase++){
        int n,k;
        cin>>n>>k;
        while(!q.empty()){
            q.pop();
        }
        int ans1,ans2;
        if(n % 2 == 0){
            ans1 = n / 2;
            ans2 = (n / 2) - 1;
        }
        else{
            ans1 = n/2;
            ans2 = ans1;
        }
        q.push(ans1);
        q.push(ans2);
        for(int i = 2; i <= k; i++){
            int val = q.top();
            q.pop();
            if(val % 2 == 0){
                ans1 = val / 2;
                ans2 = (val / 2) - 1;
            }
            else{
                ans1 = val / 2;
                ans2 = ans1;
            }
            q.push(ans1);
            q.push(ans2);
        }
        printoutput(testcase,ans1,ans2);
    }
    return 0;
}
