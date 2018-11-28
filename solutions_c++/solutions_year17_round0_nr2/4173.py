#include <bits/stdc++.h>
#define mod 10000000007
using namespace std;

vector<int> number;
void reset(){
    number.clear();
}
void fillVector(string s){
    for(int i = 0 ; i < s.length() ; i++){
        number.push_back(s[i]-'0');
    }
    for(int i = 0 ; i < number.size(); i++){
        if(number[i]==0){
            number.pop_back();
        }else{
            break;
        }
    }
}
bool tidy(int start){
    for(int i = start ; i > 0 ; i--){
        if(number[i] < number[i-1]){
            return false;
        }
    }
    return true;
}
void getOne(int start){
  if(number[start] == 0){
      number[start]=9;
      getOne(start-1);
  }else{
      number[start]--;
  }

}

int main()
{
    freopen ("C:\\Users\\Muhammed\\ClionProjects\\B-large.in","r",stdin);
    freopen ("C:\\Users\\Muhammed\\ClionProjects\\B-large.out","w",stdout);
    int tests ;
    cin >> tests;
    int counter;
    counter = 1;
    while(tests--){
        string s;
        reset();
        cin >> s  ;
        fillVector(s);
        int start = number.size()-1;
        while(!tidy(start)){
            number[start] = 9;
            getOne(start-1);
            start--;
        }
        int itStart = 0;
        for(int i = 0 ; i < number.size() ; i++){
            if(number[i]==0){
                itStart++;
            }else{
                break;
            }
        }
        cout << "Case #"<<counter<<": ";
        for(int i = itStart ; i < number.size() ; i++){
            cout << number[i];
        }
        cout << endl;
        counter++;
    }
}
