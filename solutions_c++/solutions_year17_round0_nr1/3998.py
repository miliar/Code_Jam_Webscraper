#include"iostream"
#include"string"

using namespace std;

int main(){
  int times,t=0;
  cin >> times;
  while(times--){
    t++;
    int out=0,K;
    string s;
    cin >> s >> K;
    for(int i=0;i<s.length();i++){
      if(s[i]=='-' && (s.length()-i)>=K){
        out++;
        for(int j=i;j<i+K;j++){
          if(s[j]=='-')s[j]='+';
          else s[j]='-';
        }
      }else if(s[i]=='-'){
        out=-1;
        break;
      }
    }
    cout << "Case #" << t << ": ";
    if(out==-1)cout << "IMPOSSIBLE" << endl;
    else cout << out << endl;
  }
  return 0;
}
