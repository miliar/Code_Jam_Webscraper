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
    int Ls;
    int Rs;
    int loc;

    node(int l,int r,int loc){
        this->Ls=l;
        this->Rs=r;
        this->loc=loc;
    }
};
/*
Author: Utkarsh Verma
Email ID: utkarsh13103453cse@gmail.com
Contact: +91 9871271616

*/


bool tareeka(pair<node,int> s1,pair<node,int> s2){
    if(s1.second>s2.second){
        return true;
    }else if(s1.second<s2.second){
        return false;
    }else{
        if((s1.first.Ls+s1.first.Rs)>(s2.first.Ls+s2.first.Rs)){
                return true;
        }else if((s1.first.Ls+s1.first.Rs)<(s2.first.Ls+s2.first.Rs)){
            return false;
        }else{
            if(s1.first.loc<s2.first.loc){
                return true;
            }else{
            return false;
            }
        }
    }
}


int cal_ls(string stalls,int i){
    i-=1;
    int ls=0;
    while(i>-1 && stalls[i]=='s'){
        i--;
        ++ls;
    }
    return ls;
}
int cal_rs(string stalls,int i){
    i+=1;
    int rs=0;
    while(i<stalls.size() && stalls[i]=='s'){
        i++;
        ++rs;
    }
    return rs;
}

int MIN(int a,int b){
return(a>b?b:a);
}
int MAX(int a,int b){
return(a<b?b:a);
}

node findMinMax(vector<node> &stall_list){
    vector< pair<node,int> >minMax;
    for(int i=0;i<stall_list.size();i++){
        minMax.push_back(make_pair(stall_list[i],MIN(stall_list[i].Ls,stall_list[i].Rs)));
    }
    sort(minMax.begin(),minMax.end(),tareeka);
    return minMax[0].first;
}

node func(int N,int K){
    N+=2;
    string stalls;
    int i=1;
    stalls.push_back('o');
    while(i<(N-1)){
        stalls.push_back('s');
        i++;
    }
    stalls.push_back('o');
//    cout<<stalls;
    vector<node> stall_list;
    node stall(-1,-1,-1);
    while(K>0){
        stall_list.clear();
        for(int i=0;i<N;i++){
            if(stalls[i]=='s'){
                    node temp(cal_ls(stalls,i),cal_rs(stalls,i),i);
                    stall_list.push_back(temp);
//                    cout<<temp.Ls<<"  "<<temp.Rs<<endl;
                }
        }

        K--;
        stall=findMinMax(stall_list);
        stalls[stall.loc]='o';
//        cout<<endl<<stalls<<endl;
    }
    return stall;
}

//int main(){
//node n=func(1000,1);
//cout<<endl<<n.Ls<<" "<<n.Rs;
//
//}


int main()
{
  ifstream infile;
  ofstream outfile;
  infile.open ("small_input_stall.txt");
  outfile.open("small_output_stall.txt");
  string s;
  int N;
  //getline(infile,s);
  infile>>N;
  for(int i=1;i<=N;i++)
  {
    int N,K;

    infile>>N;
    infile>>K;
    node ans=func(N,K);

    outfile<<"Case #"<<i<<": "<<MAX(ans.Ls,ans.Rs)<<" "<<MIN(ans.Ls,ans.Rs)<<endl;
  }

  //cout<<s;
  //outfile<<s;
  infile.close();
  outfile.close();
return 0;
}
