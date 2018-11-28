#include <iostream>
#include <vector>
#include <map>
#include <map>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <stack>
#include <deque>

#define LL long long
#define in cin
#define out cout

using namespace std;

int limit ;

char ChangeSymbole(char ch){
    if(ch == '+')
        return '-';
    else
        return '+';
}

void Flip(deque<char> &dqu){
    stack<char> st;
    int counter=0;
    while(!dqu.empty() && counter < limit){
        st.push(ChangeSymbole(dqu.front()));
        dqu.pop_front();
        counter++;
    }

    while(!st.empty()){
        dqu.push_front(st.top());
        st.pop();
    }
}

void Print(deque<char> d){
    cout<< "Deque " <<endl;
    while(!d.empty()){
        cout<< d.front() <<" ";
        d.pop_front();
    }
    cout<< endl <<endl;
}

int MinimumChange(deque<char> &dqu ,int len){

    if(dqu.empty())
        return 0;

    if(len < limit)
        return -1000000;

//    Print(dqu);

    while(!dqu.empty() && dqu.front() == '+'){
        dqu.pop_front();len--;
    }
    while(!dqu.empty() && dqu.back() == '+'){
        dqu.pop_back();len--;
    }

    if(dqu.empty())
        return 0;

    if(len < limit)
        return -1000000;

    Flip(dqu);

//    Print(dqu);

    while(!dqu.empty() && dqu.front() == '+'){
        dqu.pop_front();len--;
    }
    while(!dqu.empty() && dqu.back() == '+'){
        dqu.pop_back();len--;
    }

    if(dqu.empty())
        return 1;

    if(len < limit)
        return -1000000;

//    int tmp;
//    cin>>tmp;


    return 1+MinimumChange(dqu,len);

}

int main(){

    ifstream in("A-large.in");
    ofstream out("Output.txt");


    int t;in>>t;



    for(int kase = 1 ; kase <= t ; kase++ ){


        string str; in>>str;
        in>>limit;

        int len = str.length();

        deque<char> dqu;

        for ( int i = 0 ; i < len ; i++ ){
            dqu.push_back(str[i]);
        }

        int ans = MinimumChange(dqu,len);

        out<<"Case #"<<kase<<": ";
        if(ans >= 0){
            cout<< ans <<endl;
        }else{
            cout<< "IMPOSSIBLE" <<endl;
        }
    }
    return 0;
}

