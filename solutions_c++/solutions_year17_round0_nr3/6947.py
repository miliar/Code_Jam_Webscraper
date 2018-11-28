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


struct  BATHSTALL
{
    int occupied;
    int left;
    int right;

    int min() {
        return left<right?left:right;
    }
    int max() {
        return left>right?left:right;
    }
};
class CBathroomStalls
    : public CCaseInput
{
    std::vector<BATHSTALL>  m_stalls;
    void dump() {
        for(int i=0;i<m_stalls.size();++i) {
            printf("%d(%d: %d,%d) ",i,m_stalls[i].occupied,m_stalls[i].left,m_stalls[i].right);
        }
        printf("\n");
    }
    int find_max() {
        int num=m_stalls.size();
        int max=-1,idx=-1,idx_max;
        for(int i=0;i<num;++i) {
            if(m_stalls[i].occupied)
                continue;
            if(m_stalls[i].min()>max) {
                max=m_stalls[i].min();
                idx=i;
                idx_max=m_stalls[i].max();
            } else if(m_stalls[i].min()==max) {
                if(m_stalls[i].max()>idx_max) {
                    idx=i;
                    idx_max=m_stalls[i].max();
                }
            }
        }
        return idx;
    }
public:
    void solve(int caseno,const char* casetext) {
        char sz[1024];
        strncpy(sz,casetext,sizeof(sz));

        int k=0,n=atoi(sz);
        char* p=(char*)strchr(sz,' ');
        if(!p) {
            return;
        }
        k=atoi(p+1);

        if(k>n) return;
        if(n>1000000) return;
        if(k<1) return;

        m_stalls.clear();
        int i;
        BATHSTALL s;
        s.occupied=1;
        s.left=0;
        s.right=n;
        m_stalls.push_back(s);
        s.left=-1;
        for(i=0;i<n;++i) {
            s.occupied=0;
            s.left++;
            s.right--;
            m_stalls.push_back(s);
        }
        s.occupied=1;
        s.left++;
        m_stalls.push_back(s);
        //        dump();


        int min,max,idx;
        for(i=0;i<k;++i) {
            idx=find_max();
            m_stalls[idx].occupied=1;

            int j;
            // (idx,n], change left
            for(j=idx+1;j<n+1;++j) {
                if(m_stalls[j].occupied)
                    break;
                m_stalls[j].left=j-idx-1;
            }

            // (0,idx), change right
            for(j=idx-1;j>0;--j) {
                if(m_stalls[j].occupied)
                    break;
                m_stalls[j].right=idx-1-j;
            }
            //            dump();
        }
        printf("Case #%d: %d, %d\n",caseno+1,m_stalls[idx].max(),m_stalls[idx].min());
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
    CBathroomStalls flipper;
    if(!flipper.read(fpIn)) {
        printf("invalid input!\n");
        return 0;
    }
    flipper.solve();
    getchar;
    return 1;
}
