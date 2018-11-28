
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


void solveA()
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
        vector<string> s = split(line,' ');
        int D = toInt(s[0]);
        int N = toInt(s[1]);
        int Ks[N],Ss[N];
        for(int i=0;i<N;i++)
        {
            getline(myfile,line);
            vector<string> s = split(line,' ');
            Ks[i] = toInt(s[0]);
            Ss[i] = toInt(s[1]);
        }
        double max = 0;
        
        for(int j=0;j<N;j++)
        {
            double t = timeToDis(Ks[j],Ss[j],D);
            if(t > max)
                max = t;
        }
        cout << max << endl;
        double speed = (double)D/max;
        char sp[80];
        sprintf(sp,"%.6f",speed);
        
        cout << "Case #" << l+1 << ": " << sp <<  endl;
        out << "Case #" << l+1 << ": " <<  sp << endl;
        
    }
    myfile.close();
  }
}


int main(int argc, char** argv) 
{
    string line = "khobz";
    solveA();
    //cmpFiles();
    return 0;
}

