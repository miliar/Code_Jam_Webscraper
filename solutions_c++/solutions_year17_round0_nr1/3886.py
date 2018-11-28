#include <bits/stdc++.h>

using namespace std;

int solve(vector<bool> bits, int N)
{
  queue<int> flips;
  int ans= 0;
  for (int i=0;i<bits.size();i++)
  {
    if (!flips.empty()&&flips.front()<=i-N)
      flips.pop();
    if ((bits[i]^(flips.size()%2==0))==1)
    {
      if (i>bits.size()-N)
        return -1;
      flips.push(i);
      ans++;
    }
  }
  return ans;
}
int main()
{
    int t;
    cin>>t;
    int n=t;
    vector <int>ans;
    while(t>0){
    string s;
    cin>>s;
    int k;
    cin>>k;
    vector<bool> bits;

    for(int i=0;i<s.length();i++){
        if(s[i]=='-'){
            bits.push_back(false);
        }
        else{
            bits.push_back(true);
        }
    }
       ans.push_back(solve(bits,k));
       t--;
    }
    ofstream myfile;
    myfile.open ("solution.txt");

    for(int i=0;i<ans.size();i++){
        if(ans[i]!=-1){
        myfile<<"Case #"<<i+1<<": "<<ans[i]<<endl;
       }
       else
        myfile<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    }
        myfile.close();

    return 0;
}
