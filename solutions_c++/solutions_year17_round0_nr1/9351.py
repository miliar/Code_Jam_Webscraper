#include<iostream>
#include <fstream>

using namespace std;

void solve(string& sample, int spatLnght, bool& possible, int& moves);
void flipSegment(int spatlngth, string& sample, int index);
bool solved(const string &sample);


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int testcase,spatLnght;
    string sample;
    bool possible;
    int moves = 0;

    cin>>testcase;

    for(int i = 0; i < testcase; i++){
        cin>>sample;
        cin>>spatLnght;

        solve(sample, spatLnght, possible, moves);

        if(possible)
            cout<<"Case #"<<i+1<<": "<<moves<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        moves = 0;
    }
    return 0;
}


void solve(string& sample, int spatLnght, bool& possible, int& moves){

    for(int i = 0; i < sample.length(); i++){
        if(sample[i] == '-'){
            moves++;
            flipSegment(spatLnght, sample, i);
        }
    }
    possible = solved(sample);
}

void flipSegment(int spatlngth, string& sample, int index){

    if(index+spatlngth > sample.length())
        return;

    for(int i = index; i < index+spatlngth; i++)
        (sample[i] == '+') ? (sample[i] = '-') : (sample[i] = '+');

}

bool solved(const string &sample){

    bool solved = true;

    for(int i = 0; i < sample.size(); i++){
        if(sample[i] == '-'){
            solved = false;
            break;
        }
    }

    return solved;

}


