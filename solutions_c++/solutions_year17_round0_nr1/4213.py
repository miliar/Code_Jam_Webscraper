#include <bits/stdc++.h>
#define mod 10000000007
using namespace std;

int steps;
void reset(){
    steps = 0;
}

void solve(string s ){
    int i = 0 , j = s.length()-1;
    while(i < s.length()){
        if(s[i]=='-')
            break;
        i++;
    }
    while(j >= 0){
        if(s[j]=='-')
            break;
        j--;
    }
    if(j < i)
        return ;
    if( i > 0){
        for(int k = 0 ; k < i ; k++){
            s[k]='-';
        }
        steps++;
    }
    i=0;
    if(j >= i){
        steps++;
        string t = s;
        while(j >= i){
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            if(s[i]=='-'){
                s[i]='+';
            }else{
                s[i] = '-';
            }
            if(i != j){
                if(s[j]=='-'){
                    s[j]='+';
                }else{
                    s[j] = '-';
                }
            }
            i++;
            j--;
        }
    }
    solve(s);

}

int main()
{
    freopen ("C:\\Users\\Muhammed\\ClionProjects\\A-large.in","r",stdin);
    freopen ("C:\\Users\\Muhammed\\ClionProjects\\A-large.out","w",stdout);
    int tests ;
    cin >> tests;
    int counter;
    counter = 1;
    while(tests--){
        string s;
        int n ;
        reset();
        cin >> s >> n ;
        bool bad = false;
        int steps  = 0;
        for(int i = 0 ; i < s.length() ; i++){
            if(s[i]=='-'){
                if(i+n > s.length()){
                    bad = true;
                    break;
                }
                steps++;
                for(int j = 0; j < n && i+j < s.length(); j++){
                    if(s[i+j]== '-'){
                        s[i+j]='+';
                    }else{
                        s[i+j]='-';
                    }
                }
            }
        }
        if(!bad)
            cout << "Case #"<< counter << ": "<< steps << endl;
        else
            cout << "Case #"<<counter<<": IMPOSSIBLE" << endl;
        counter++;
    }
}