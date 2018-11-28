#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");

struct panc{
    int r;
    int h;
    double l;
};

vector<panc >pancakes;//rad,height
bool used[1000];

double inline calculateStart(int r,int h){
    return M_PI*r*r+M_PI*2*r*h;
}

double inline calculateLateral(int r,int h){
    return M_PI*2*r*h;
}

int main()
{
    int caso,ncasi,n,k;
    in>>ncasi;
    FILE * pFile;
    pFile = fopen ("out.out","w");
    vector<double> lateralArea;
    for (caso=1;caso<=ncasi;caso++){
        double area=0,maxArea=0;
        pancakes.clear();
        lateralArea.clear();
        in>>n>>k;
        for (int i=0;i<n;i++){
            panc tmp;
            in>>tmp.r>>tmp.h;
            tmp.l=calculateLateral(tmp.r,tmp.h);
            pancakes.push_back(tmp);
        }
        for (int i=0;i<n-1;i++){
            for (int j=0;j<n-i-1;j++){
                if (pancakes.at(j).l<pancakes.at(j+1).l){
                    panc tmp;
                    tmp=pancakes.at(j);
                    pancakes.at(j)=pancakes.at(j+1);
                    pancakes.at(j+1)=tmp;
                }
            }
        }
        int firstSize;
        for (int i=0;i<n;i++){
            area=calculateStart(pancakes.at(i).r,pancakes.at(i).h);
            firstSize=pancakes.at(i).r;
            int inserted=1;
            for (int j=0;j<n&&inserted<k;j++){
                if (j!=i&&pancakes.at(j).r<=firstSize){
                    area+=pancakes.at(j).l;
                    inserted++;
                }
            }
            if (area>maxArea&& inserted==k) maxArea=area;
        }
        fprintf (pFile, "Case #%d: %f\n",caso,maxArea);
    }
    return 0;
}
