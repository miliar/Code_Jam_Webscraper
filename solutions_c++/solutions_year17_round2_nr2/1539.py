
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

double timeToDis(int pos,int s,int dis)
{
    double rDis = dis - pos;
    double t = rDis / (double) s;
    return t;
}


void solveB()
{
      string line;
  ifstream myfile ("B-small-attempt0.in");
  ofstream out;
  out.open("jamOut.txt");
  
  int mat[6][6] = 
  {
    0,0,1,1,1,0,
    0,0,0,0,1,0,
    1,0,0,0,1,1,
    1,0,0,0,0,0,
    1,1,1,0,0,0,
    0,0,1,0,0,0
  };
  int next[6] = {3,4,5,0,1,2}; 
  char cols[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
  if (myfile.is_open())
  {
    getline (myfile,line);
    int size = toInt(line);
    for(int l=0;l<size;l++)
    {
        getline(myfile,line);
        vector<string> s = split(line,' ');
        string sol ="";
        int N = toInt(s[0]);
        int Colors[6];
        for(int i=0;i<6;i++)
            Colors[i] = toInt(s[i+1]);
        int current = 0;
        for(;current < 6 && !Colors[current];current+=2);
        if(current == 6)
        for(current = 1;current < 6 && !Colors[current];current+=2); 
        if(current == 6)
            return;
        
        Colors[current]--;
        int start = current;
        sol += cols[current];
        N--;
        bool correct = false;

        for(int i=0;i<N;i++)
        {            
            int ne = next[current];
            if(Colors[ne])
            {
                current = ne;
                Colors[ne]--;
                sol += cols[ne];
            }
            else
            {
                int max = 0;
                int maxInd = -1;
                for(int j=0;j<6;j++)
                    if(mat[current][j] && max < Colors[j])
                    {
                        max = Colors[j];
                        maxInd = j;
                    }
                if(maxInd == -1)
                    break;
                current = maxInd;
                Colors[maxInd]--;
                sol += cols[maxInd];
            }
                if(i==N-1)
                    for(int j=0;j<6;j++)
                        if(mat[current][j] && j == start)
                        {
                            correct = true;
                            break;
                        }
        }
        if(correct)
        {
        cout << "Case #" << l+1 << ": " << sol <<  endl;
        out << "Case #" << l+1 << ": " <<  sol << endl;
        }
        else
        {
        cout << "Case #" << l+1 << ": IMPOSSIBLE"  <<  endl;
        out << "Case #" << l+1 << ": IMPOSSIBLE"  << endl;            
        }
        
    }
    myfile.close();
  }
}


int main(int argc, char** argv) 
{
    string line = "khobz";
    solveB();
    //cmpFiles();
    return 0;
}

