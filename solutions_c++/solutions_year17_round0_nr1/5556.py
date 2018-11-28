#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<fstream>
#include<string>
#include<list>
#include<stack>
#include<unordered_set>

using namespace std;


class node{
public:
    node *next;
    node *pre;
    int val;
    string str;

    node(int v,string s){
        this->val=v;
        this->str=s;
        this->next=NULL;
        this->pre=NULL;
    }
};
/*
Author: Utkarsh Verma
Email ID: utkarsh13103453cse@gmail.com
Contact: +91 9871271616

*/

long long int countSad(string cakes){
long long int countSad=0;
for(int i=0;i<cakes.length();i++){
if(cakes[i]=='-'){
countSad++;
}
}
return countSad;
}

long long int func(string cakes, long long int K){
    long long int c=countSad(cakes);
    long long int ans=0;

    for(long int i=0;i<cakes.length() && (c>1);i++){
        //cout<<"in for: "<<i<<" c:"<<c<<" cakes: "<<cakes<<endl;

        if(cakes[i]=='-' && i+K<=cakes.length()){

            for(long int j=i;j<i+K;j++){
                cakes[j]=(cakes[j]=='+')?'-':'+';

                }
                ans++;
            }else if(cakes[i]=='-' && i+K>cakes.length()){
            return -1;
            }
            c=countSad(cakes);
        }



    if(c==1 && K>1){
    return -1;
    }else if(c==0){
    return (ans);
    }else{
    return -2;
    }
}

int main()
{
  ifstream infile;
  ofstream outfile;
  infile.open ("small_input.txt");
  outfile.open("small_output.txt");
  string s;
  int N;
  //getline(infile,s);
  infile>>N;
  for(int i=1;i<=N;i++)
  {
    cout<<"case: "<<i<<endl;
    long long int ans=0;
    string cakes;
    infile>>cakes;
    int K;
    infile>>K;
    ans=func(cakes,K);
    if(ans==-1){
    outfile<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }else{
    outfile<<"Case #"<<i<<": "<<ans<<endl;
    }
  }

  //cout<<s;
  //outfile<<s;
  infile.close();
  outfile.close();
return 0;
}
