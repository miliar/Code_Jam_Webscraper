#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve(string row);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<":\n";
    int rows,cols;
    cin>>rows>>cols;

    vector<string> cake(rows);
    for(int i=0;i<cake.size();i++)
      cin>>cake[i];

    string last_row;
    int reuse=0;
    for(int r=0;r<rows;r++){
      if(cake[r]==string(cols,'?')){
        reuse++;
        continue;
      }

      string s=solve(cake[r]);

      for(int i=0;i<=reuse;i++)
        cout<<s<<'\n';

      last_row=s;
      reuse=0;
    }

    for(int i=0;i<reuse;i++)
      cout<<last_row<<'\n';
  }
}

string solve(string row){
  char last='?';
  for(int i=0;i<row.size();i++)
    if(row[i]!='?'){
      last=row[i];
      break;
    }

  for(int i=0;i<row.size();i++){
    if(row[i]=='?')
      row[i]=last;
    else
      last=row[i];
  }

  return row;
}
