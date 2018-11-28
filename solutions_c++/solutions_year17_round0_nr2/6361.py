/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: ressay
 *
 * Created on 08 March 2017, 12:14
 */

#include <gmpxx.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 
#include <vector>
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

void solveCredit()
{
      string line;
  ifstream myfile ("A-large-practice.in");
  ofstream out;
  out.open("jamOut.txt");
  
  if (myfile.is_open())
  {
    getline (myfile,line);
    int size = toInt(line);
    for(int i=0;i<size;i++)
    {
        getline (myfile,line);
        int credit = toInt(line);
        getline (myfile,line);
        int numPro = toInt(line);
        getline (myfile,line);
        vector<string> strs = split(line,' ');
        vector<int> products;
        for(int j=0;j<strs.size();j++)
            products.push_back(toInt(strs[j]));

        for(int j=0;j<products.size();j++)
            for(int k=j+1;k<products.size();k++)
                if(products[j]+products[k] == credit)
                {
                    cout << "Case #" << i+1 << ": " << j+1 << " " << k+1 << endl;
                    out << "Case #" << i+1 << ": " << j+1 << " " << k+1 << endl;
                }
    }
    myfile.close();
  }
}


void solveTidy()
{
      string line;
  ifstream myfile ("B-large.in");
  ofstream out;
  out.open("jamOut.txt");
  
  if (myfile.is_open())
  {
    getline (myfile,line);
    int size = toInt(line);
    for(int l=0;l<size;l++)
    {
        getline(myfile,line);
        
        string output = "";
        string fline = string(line);
        bool end = false;
        for(int i=0;i<line.size()-1;i++)
        {
            while(i >= 0 && line[i] > line[i+1])
            {
                end = true;
                line[i]--;
                i--;
            }
            if(end)
            {
                i+=2;
                for(;i<line.size();i++)
                    line[i] = '9';
            }
        }
        if(line[0] == '0')
        {
            string s = "";
            for(int i=0;i<line.size()-1;i++)
                s+="9";
            line = s;
        }
        cout << "Case #" << l+1 << ": " << endl << fline << endl << line << endl;
        out << "Case #" << l+1 << ": " << line << endl;
        
    }
    myfile.close();
  }
}

void solvePan()
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
        getline (myfile,line);
        
        vector<string> strs = split(line,' ');
        string pans = strs[0];
        int k = toInt(strs[1]);
        int numTimes=0;
//        cout << "k is " << k << endl;
        for(int i=0;i<=pans.size()-k;i++)
        {
            if(pans[i] == '-')
            {
                for(int j=0;j<k;j++)
                    if(pans[i+j] == '-')
                        pans[i+j] = '+';
                    else 
                        pans[i+j] = '-';
                numTimes++;
            }
//            cout << pans << endl;
        }
        cout << "Case #" << l+1 << ": ";
        out << "Case #" << l+1 << ": ";
        int i=0;
        for(;i<pans.size() && pans[i] == '+';i++);
        if(i < pans.size())
        {
            cout << "IMPOSSIBLE";
            out << "IMPOSSIBLE";
        }
        else
        {
            cout << numTimes;
            out << numTimes;
        }
        cout << endl;
        out << endl;

    }
    myfile.close();
  }
}


int main(int argc, char** argv) 
{
    solveTidy();

    return 0;
}

