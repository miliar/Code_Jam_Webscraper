#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class inc
{
public:
    long long int begin = -1;
    long long int answer;
    
    vector<long long int> getdig(long long int num);
    long long int getnum(vector<long long int> dig);
    bool isincreasing(long long int num);
    bool contains (vector<long long int> dig, int d);
    int begin_notincreasing(vector<long long int> dig);
    //void perform(vector<long long int> dig); 
    void perform(long long int num);
};

vector<long long int> inc::getdig(long long int num)
{
    vector<long long int> dig;
    
    while (num > 0)
    {
        dig.push_back(num % 10);
        num /= 10;
    }
    
    reverse(dig.begin(), dig.end());
    
    return dig;
}

/*long long int inc::getnum(vector<long long int> dig)
{
    reverse(dig.begin(), dig.end());
    long long int sum = 0;
    for(long long int i = 0; i < dig.size(); i++)
        sum += dig.at(i) * pow(10, i);
    
    return sum;
}*/

bool inc::isincreasing(long long int num)
{
    int count = 0;
    vector<long long int> vl = getdig(num);
    
    for(int i = 0; i < vl.size() - 1; i++)
    {
        if(vl.at(i) > vl.at(i + 1))
            break;
        else
            count ++;
    }
   
    
    return (count == vl.size() - 1);
}

void inc::perform(long long int num)
{
    for(int i = num; i > 0; i--)
    {
        if(isincreasing(i))
        {
            answer = i;
            break;
        }
    }
}

/*
bool inc::contains(vector<long long int> dig, int d)
{
    for(int i = 0; i < dig.size(); i++)
        if(dig.at(i) == d) return true;
    
    return false;
}

int inc::begin_notincreasing(vector<long long int> dig)
{
    for(int i = 0; i < dig.size(); i++)
    {
        if(dig.at(i) > dig.at(i + 1))
        {
            begin = i;
            break;
        }
    }
    
    return begin;
}

void inc::perform(vector<long long int> dig)
{
    long long int x = getnum(dig);
    if(isincreasing(x)) answer = x;
    else
    {
        begin = begin_notincreasing(dig);
        
        if(contains(dig, 0))
        {
            int start = dig.at(0);
            dig.at(0) = start - 1;
            
            for(int i = 1; i < dig.size(); i++)
                dig.at(i) = 9;
            
            long long int z = getnum(dig);
            
            answer = z;
        }
        
        else
        {
            dig.at(begin) = dig.at(begin + 1);
            dig.at(begin + 1) = 9;
            perform(dig);
        }
        
    }
}*/

int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("out.txt");
    
    vector<long long int> vi;
    
    string s;
    getline(fin, s);
    string::size_type sz;
    int T = stoi(s, &sz);
    
    for(int i = 0; i < T; i++)
    {
        inc in;
        
        string str;
        getline(fin, str);
        string::size_type sz1;
        long long int x = stoll(str, &sz1);
        
        in.perform(x);
        vi.push_back(in.answer);
    }
    
    for(int i = 0; i < vi.size(); i++)
        fout << "Case #" << i + 1 << ": " << vi.at(i) << endl;
    
    fin.close();
    fout.close();  
}