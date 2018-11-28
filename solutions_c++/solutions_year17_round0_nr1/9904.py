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
/*
void play(std::string str, int window,int depth){
    if(goaled(str)){
         //std::cout<<depth<< " ";
         counter.push_back(depth);
    }
    else{
    global_visits.push_back(str);
    int c = 0;

    list<string> localV;
    string strDup = str;
    while(c<=(str.length()-window)){
        str = strDup;
        for(int j=c; j<=(c+window-1); j++){
            //cout<<j;
            if(str[j]=='+')
                str[j] = '-';
            else
                str[j] = '+';

        }

        if(findingStr(str)){
            //std::cout<<c<< " ";
            //std::cout<<str<< " "<<endl;
        }
        else{
                //cout<<str<<endl;
               localV.push_back(str);
        }

        c++;
    }
            std::list<std::string>::iterator iter;

    for(iter = localV.begin(); iter != localV.end(); ++iter)
    {
        play(*iter,window,depth+1);
    }



    }
} */
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
         //std::cout<<deptCurr<< "ff ";
         found++;
         break;
        // counter.push_back(depth);
    }
    else{

    int c = 0;


    string strDup = str;
    while(c<=(str.length()-window)){
        str = strDup;
        for(int j=c; j<=(c+window-1); j++){
            //cout<<j;
            if(str[j]=='+')
                str[j] = '-';
            else
                str[j] = '+';

        }

        if(findingStr(str)){
            //std::cout<<c<< " ";
            //std::cout<<str<< " "<<endl;
        }
        else{
              //  cout<<str<<" "<<deptCurr;
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

    ofstream outp;
    outp.open("A-small-output.txt");
    ifstream inp;
    inp.open("A-small-attempt0.in");

    if(1){
        inp>>t;
      //      cin>>t;
        for(int i=0; i<t; i++){
            inp>>s>>k;
            //cin>>s>>k;
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
            //cout<<"Case #"<<i+1<<": ";
            if(found <1){
                outp<<"IMPOSSIBLE"<<endl;
                //cout<<"IMPOSSIBLE"<<endl;
            }
            else
            {
                outp<<deptCurr<<endl;
                //cout<<*std::min_element(counter.begin(), counter.end())<<endl;
            }
        }
    }else{

}
inp.close();
outp.close();



  return 0;
}
