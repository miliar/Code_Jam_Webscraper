#include <iostream>
#include <algorithm> 
#include <queue>
#include <vector>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
using namespace std;

struct node
{
	int data=0;
	node* next=NULL;
};

char ch(int n)
{
	if(n==1) return 'R';
	if(n==2) return 'Y';
	if(n==4) return 'B';
	if(n==3) return 'O';
	if(n==6) return 'G';
	if(n==5) return 'V'; 
	return '\n';
}

int main()
{
	int T,n,a[7],check,x=0;
	node *head,*tmp,*ttmp,*nhead;
	scanf("%d",&T);
	while(T--)
	{
		head = new(node),nhead=NULL;
		scanf("%d%d%d%d%d%d%d",&n,&a[1],&a[3],&a[2],&a[6],&a[4],&a[5]);
		for(tmp=head;a[1];tmp=tmp->next)
			a[1]--,tmp->data=1,tmp->next=new(node);
		for(tmp=head;tmp->data!=0 && a[2];nhead=ttmp,tmp=ttmp->next)
			a[2]--,ttmp=new(node),ttmp->data=2,ttmp->next=tmp->next,tmp->next=ttmp;
		if(tmp->data!=0) nhead=tmp;
		if(nhead==NULL) nhead=head;
		for(;a[2];tmp=tmp->next)
			a[2]--,tmp->data=2,tmp->next=new(node);
		for(tmp=nhead;tmp->data!=0 && a[4];tmp=ttmp->next)
			a[4]--,ttmp=new(node),ttmp->data=4,ttmp->next=tmp->next,tmp->next=ttmp;
		//if(tmp->data==0 && a[4]) a[4]--,tmp->next=new(node),tmp->data=4;
		for(tmp=head;tmp->data!=0 && a[4];tmp=ttmp->next)
			a[4]--,ttmp=new(node),ttmp->data=4,ttmp->next=tmp->next,tmp->next=ttmp;
		//for(ttmp=head;ttmp!=NULL;ttmp=ttmp->next) printf("%c",ch(ttmp->data));
		if(tmp->data==0)
		{
			printf("Case #%d: IMPOSSIBLE\n",++x);
			for(;head!=NULL;tmp=head,head=head->next,delete tmp) ;
			continue;
		}
		for(check=head->data,tmp=head->next;tmp->data!=0;check=tmp->data,tmp=tmp->next)
			if(tmp->data==check) break;
		if(tmp->data!=0 || check==head->data)
		{
			printf("Case #%d: IMPOSSIBLE\n",++x);
			for(;head!=NULL;tmp=head,head=head->next,delete tmp) ;
			continue;
		}
		else
		{
			printf("Case #%d: ",++x);
			for(;head!=NULL;tmp=head,head=head->next,delete tmp) printf("%c",ch(head->data));
		}
	}
}
