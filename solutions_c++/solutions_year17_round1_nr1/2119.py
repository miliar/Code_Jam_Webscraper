#include <iostream>
#include <vector>

using namespace std;

void copy_row(const int r1, const int r2, const int c, vector<vector<int> >&table){
  for(int j=0; j<c; j++)
    table[r2][j] = table[r1][j];
  return;
}


int main(){
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  int r, c, i, j;
  char code;
  string s;
  for(int ind=0; ind<T; ind++){
    cin >> r >> c;
    vector<vector<int> >table(r, vector<int>(c, -1));
    vector<int>counter_row(r, 0);
    for(i=0; i<r; i++){
      cin >> s;
      //cout << s << endl;
      for(j=0; j<c; j++){
       code = s[j];
        if(code-'A'>=0 && 'Z'-code>=0){
          table[i][j] = code-'A';
          counter_row[i]++;
        }
      }
    }
    int first,last;
    for(i=0; i<r; i++)
      if(counter_row[i]>0){
        //cout << "filling row i = " << i << endl;
        for(first=0; first<c && table[i][first]<0; first++);
        for(j=0; j<first; j++) table[i][j] = table[i][first];
        last=table[i][first];
        for(j=first+1; j<c; j++){
          
          if(table[i][j]>=0) last = table[i][j];
          else table[i][j] = last;
        }
      }
    for(first=0; first<r && counter_row[first]==0; first++);
    for(i=0; i<first; i++)
      copy_row(first, i, c, table);
    last = first;
    for(i=first+1; i<r; i++){
      if(counter_row[i]>0) last = i;
      else copy_row(last, i, c, table);
    }
    cout << "Case #" << (ind+1) << ": " << endl;
    for(i=0; i<r; i++){
      for(j=0; j<c; j++){
        cout << (char)('A'+table[i][j]);
      }
      cout << endl;
    }
  }
  return 0;
}