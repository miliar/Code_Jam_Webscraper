//
//  main.m
//  Pancake-Flipper
//
//  Created by Libing Ban on 09/04/2017.
//  Copyright © 2017 Libing Ban. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>

class CCaseInput
{
protected:
    int m_num;
    std::vector<std::string>    m_cases;

public:
    int read(FILE* fpIn) {
        char sz[1024];
        if(fgets(sz,sizeof(sz),fpIn))
            m_num=atoi(sz);

        if(m_num<1 || m_num>100)
            return 0;

        while(fgets(sz,sizeof(sz),fpIn)) {
            m_cases.push_back(sz);
            if(m_cases.size()==m_num)
                return 1;
        }
        return 0;
    }
};

class CPancakeFlipper
    : public CCaseInput
{
public:
    void solve(int caseno,const char* casetext) {
        char sz[1024];
        strncpy(sz,casetext,sizeof(sz));

        int k=0;
        char* p=(char*)strchr(sz,' ');
        if(!p) {
            return;
        }
        k=atoi(p+1);
        *p=0;

        int len=(int)strlen(sz);
        if(len<2 || len>1000)
            return;
        if(k<2 || k>len)
            return;
        //printf("to solve: %s, k: %d\n",sz, k);
        int i,flip=0;
        bool b=true;
        for(i=0;i<len;++i) {
            if(sz[i]=='+')
                continue;
            if(i+k>len) {
                b=false;
                break;
            }
            ++flip;
            for(int j=i;j<i+k;++j) {
                if(sz[j]=='-') sz[j]='+';
                else sz[j]='-';
            }
            //printf("after flip %d: %s\n",flip,sz);
        }
        if(b) {
            printf("Case #%d: %d\n",caseno+1,flip);
        } else {
            printf("Case #%d: IMPOSSIBLE\n",caseno+1);
        }
    }
    void solve() {
        for(int i=0;i<m_num;++i) {
            solve(i,m_cases[i].c_str());
        }
    }
};

int main(int argc, const char * argv[]) {
	if(argc<2) {
		printf("Usage: %s casefile\n",argv[0]);
		return 0;
	}
    FILE* fpIn=fopen(argv[1],"r");
    CPancakeFlipper flipper;
    if(!flipper.read(fpIn)) {
        printf("invalid input!\n");
        return 0;
    }
    flipper.solve();
    system ("PAUSE");
    return 1;
}
