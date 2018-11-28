#include <iostream>
#include <string> 
#include <set>
#include <map>
#include <vector>
#include <sstream>
using namespace std;


int flip(string & pankcakes,string pattern){
    //cout << pankcakes<<endl;
    int res=0;

    //mega flips
    size_t found = pankcakes.find(pattern);
    found = pankcakes.find('-');
    if(found ==string::npos)
        return res;

    pankcakes = pankcakes.substr(found,pankcakes.rfind('-')-found+1);

    if(pankcakes.length() > 0 && pankcakes.length()  < pattern.length())
        return -1;
    
    //single flip
    for(int i=0;i<pattern.length();i++)
    {
      pankcakes[i] = pankcakes[i] == '+'?'-':'+';
    }
    ++res;

    int ret = flip(pankcakes, pattern);
    res = ret!=-1?res+ret:-1;
    return res;
        
}

int main(){
    int T;
    cin >> T;
    for (int x=0;x<T;x++){
        string pankcakes;
        int flippersize;
        cin >> pankcakes >> flippersize;
        string pattern = "";
        for(int i=0;i<flippersize;i++)
            pattern += '-';

        
       int res = flip(pankcakes, pattern);
       // cout <<  res << endl;
       string result;
       if (res == -1)
        result = "IMPOSSIBLE";
       else{
        stringstream ss;
        ss << res;
        ss >> result;        
        }
       cout << "Case #"<<x+1<<": "<<result<<endl;
    }
    return 0;
}