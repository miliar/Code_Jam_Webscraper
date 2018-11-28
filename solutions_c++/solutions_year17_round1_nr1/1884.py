
#include <gmpxx.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 
#include <vector>
#include <map>
#include <iterator>


template<typename Out>
void split(const std::string &s, char delim, Out result) {
    std::stringstream ss;
    ss.str(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        *(result++) = item;
    }
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}

using namespace std;

int toInt(string s)
{
    int x;
    stringstream convert;
    convert<<s;
    convert>>x; 
    return x;
}

mpz_class toBigInt(string s)
{
    mpz_class k=0;
    for(int i=0;i<s.size();i++)
    {
        int a = s[i] - '0';
        mpz_class e = a;
        k*=10;
        k+= e;
    }
    return k;
}

string toString(int x)
{
    string s;
    stringstream convert;
    convert<<x;
    convert>>s; 
    return s;
}

/*
 * 
 */
bool cmpFiles()
{
    ifstream myfile1 ("jamOut.txt");
    ifstream myfile2 ("jam.out");
    string line1,line2;
    
    for(int i=0;i<100;i++)
    {
        getline (myfile1,line1);
        getline (myfile2,line2);
        if(line1.compare(line2) != 0)
        {
            cout << line1 << " and " << line2 << endl;
        }
    }
}

bool expandableV(int x,int y,vector<string>& v)
{
//    cout << "expV" << endl;
    char c = v[x][y];
    int f=0,min=0,max = 0;
    for(int i=0;i<v.size();i++)
    {
        string line = v[i];
        for(int j=0;j<line.size();j++)
        {
            if(line[j] == c)
            {
                if(!f)
                {
                    f=1;
                    min = i;
                }
                if(i>max)
                    max = i;
            }
        }
    }
    bool changed = true;
    if(min > 0)
    {
    string line = v[min-1];
    for(int j=0;j<line.size() && changed;j++)
        if(v[min][j] == c)
            if(line[j] == '?')
            line[j] = c;
            else
            changed = false;
    
    if(changed)
    {
        v[min-1] = line;
        return true;
    }
    }
    changed = true;
    if(max < v.size()-1)
    {
    string line = v[max+1];
    for(int j=0;j<line.size() && changed;j++)
        if(v[max][j] == c )
            if(line[j] == '?')
            line[j] = c;
            else
            changed = false;
    
    if(changed)
    {
        v[max+1] = line;
        return true;
    }
    }
    
}

bool expandableH(int x,int y,vector<string>& v)
{
//    cout << "expH" << endl;
    char c = v[x][y];
    int f=0,min=0,max = 0;
    string line = v[0];
    for(int i=0;i<line.size();i++)
    {
        
        for(int j=0;j<v.size();j++)
        {
            if(v[j][i] == c)
            {
                if(!f)
                {
                    f=1;
                    min = i;
                }
                if(i>max)
                    max = i;
            }
        }
    }
//    cout << "expH2" << endl;
    bool changed = true;
    if(min > 0)
    {
    for(int j=0;j<v.size() && changed;j++)
        if(v[j][min] == c)
            if(v[j][min-1] != '?')
            changed = false;            
    
    if(changed)
    {
        for(int j=0;j<v.size() && changed;j++)
        if(v[j][min] == c)
            v[j][min-1] = c;
        return true;
    }
    }
//    cout << "expH3" << endl;
    changed = true;
    
    if(max < line.size()-1)
    {
    
    for(int j=0;j<v.size() && changed;j++)
        if(v[j][max] == c)
            if(v[j][max+1] != '?')
            changed = false; 
    
    if(changed)
    {
        for(int j=0;j<v.size() && changed;j++)
        if(v[j][max] == c)
            v[j][max+1] = c;
        return true;
    }
    }
//    cout << "expHEnd" << endl;
}

bool expandable(int x,int y,vector<string>& v)
{
    return expandableH(x,y,v) || expandableV(x,y,v);
    
}

void solveCake()
{
      string line;
  ifstream myfile ("A-large.in");
  ofstream out;
  out.open("jamOut.txt");
  
  if (myfile.is_open())
  {
    getline (myfile,line);
    int size = toInt(line);
    for(int l=0;l<size;l++)
    {
        getline(myfile,line);
        vector<string> v = split(line,' ');
        
        int R = toInt(v[0]);
        int C = toInt(v[1]);
        vector<string> mat;
        for(int i=0;i<R;i++)
        {   
            getline(myfile,line);
            mat.push_back(line);
        }
        
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(mat[i][j] != '?')
                while(expandable(i,j,mat));
            }
        }
        
        cout << "Case #" << l+1 << ": " <<  endl;
        out << "Case #" << l+1 << ": " <<  endl;
        for(int i=0;i<mat.size();i++)
        {
            cout <<mat[i] << endl;
            out <<mat[i] << endl;
        }
        
    }
    myfile.close();
  }
}


int main(int argc, char** argv) 
{
    string line = "khobz";
    solveCake();
    //cmpFiles();
    return 0;
}

