#include <iostream>
#include <string>
#include <iterator>
#include <list>
#include <algorithm>
#include <fstream>
using namespace std;

std::list<std::string> global_visits;
std::list<std::string> global_visits2;
list<string> mainlist;
std::list<int> counter;
int deptCurr = -1;
int found = 0;


int goaled(string strr){
    for(int i = 0; i<strr.length();i++){
        if(strr[i]=='-')
            return 0;
    }
    return 1;
}

int findingStr(string strr){
    std::list<std::string>::iterator iter;

    for(iter = global_visits2.begin(); iter != global_visits2.end(); ++iter)
    {
      if(*iter == strr){
        return 1;
      }
    }
    return 0;
}

int findingStrLocal(list<string> li, string strr){
    std::list<std::string>::iterator iter;

    for(iter = li.begin(); iter != li.end(); ++iter)
    {
      if(*iter == strr){
        return 1;
      }
    }
    return 0;
}

void play(int window){

    std::list<std::string>::iterator iter;
    string str;

    for(iter = mainlist.begin(); iter != mainlist.end(); ++iter)
    {
        global_visits.push_back(*iter);
    }
    mainlist.clear();

    for(iter = global_visits.begin(); iter != global_visits.end(); ++iter)
    {
         str = *iter;

    if(goaled(str)){

         found++;
         break;

    }
    else{

    int c = 0;


    string strDup = str;
    while(c<=(str.length()-window))
        {
        str = strDup;

        for(int j=c; j<=(c+window-1); j++)
        {

            if(str[j]=='+')
                str[j] = '-';
            else
                str[j] = '+';

        }

        if(findingStr(str)){
        }
        else
            {

               mainlist.push_back(str);
               global_visits2.push_back(str);
        }

        c++;
    }


    }
    }
    global_visits.clear();
    deptCurr++;



}

int main(){

    int t;
    int k = 0;
    std::string s = "";

    ifstream in;
    in.open("A-small-attempt0.in"); // INPUT


    ofstream outp;
    outp.open("A.txt");


    if(1){
        in>>t;

        for(int i=0; i<t; i++){
            in>>s>>k;

            global_visits.clear();
            counter.clear();
            global_visits2.clear();
            mainlist.clear();
            deptCurr = -1;
            found = 0;
            mainlist.push_back(s);
            global_visits2.push_back(s);
            while(!mainlist.empty()&&found<1)
                play(k);
            outp<<"Case #"<<i+1<<": ";

            if(found <1){
                outp<<"IMPOSSIBLE"<<endl;

            }
            else
            {
                outp<<deptCurr<<endl;

            }
        }
    }else{

}
in.close();
outp.close();



  return 0;
}
