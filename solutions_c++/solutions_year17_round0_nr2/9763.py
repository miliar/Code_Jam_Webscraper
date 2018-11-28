    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll ;

    int main(){
    ifstream fin ("B-small-attempt4.in");
    ofstream fout ("outputs2.txt");
    if(!fin.is_open()) cout<<"the input file didn't open "<<endl;
    if(!fout.is_open()) cout<<"the output file didn't open " <<endl;
    int t;
    fin>>t;
    for(int tt=1;tt<=t;tt++){
      ll n; fin>>n ;
     // fout<< n << " " ;
      vector<int> digits ;
      while(n){
        digits.push_back(n%10);
        n/=10;
      }
      int tst = 0 ;
      int i=digits.size()-1 ;
      for( ; i>0 ; i--){
          if(digits[i]>digits[i-1]){
              if(digits[i]==1 && digits[i-1]==0) tst = 1;
              if(i != digits.size()-1 && digits[i]==digits[i+1]){
  int val = digits[i]; digits[i] = 9;
  for(int u=i+1; u<digits.size() ; u++){
      if(digits[u] == val ) digits[u]--;
  }
              }else{
                 digits[i]-- ;
              }
              break ;
          }
      }

      if(tst == 1){

      fout<<"Case #"<<tt<<": ";
      for( i = 0  ; i< digits.size()-1 ; i++){
         fout<<9;
      }
      fout<<endl;
      continue ;
      }
      i--;
      for(; i>=0 ; i--){
          digits[i] = 9 ;
      }
      i = digits.size()-1;
      for( ; i>=0 && digits[i]==0 ; i--){};

      fout<<"Case #"<<tt<<": ";
      for( ; i>=0 ; i--){
         fout<< digits[i];
      }
      fout<<endl;
    }
  fin.close();
  fout.close();
       return 0 ;
    }
