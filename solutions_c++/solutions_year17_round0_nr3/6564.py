#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

struct t_node {
	unsigned long long s, l;
	t_node *next, *prev;
} *root;

unsigned long long len;

unsigned long long insert(unsigned long long olds, unsigned long long oldl, unsigned long long news, unsigned long long newl) 
{
	if(len==0)
	{
		root = new t_node;
		root->s = olds;
		root->l = oldl;
		root->prev = root->next = NULL;
		len = 1;
	} 
	else
	{
		t_node *t = root;
		while(t->s!=olds)
			t = t->next;
		t->l = oldl;

		if(newl>0)
		{
			t_node *node = new t_node;
			node->s = news;
			node->l = newl;
			node->next = t->next;
			node->prev = t;

			t->next = node;
			len++;
		}
	}
	return len;
}

void erase(unsigned long long s)
{
	t_node *node = root;
	while(node)
	{
		if(node->s == s)
		{
			if(node->prev)
			{
				node->prev->next = node->next;
				if(node->next)
					node->next->prev = node->prev;
				node->next = node->prev = NULL;
				delete node;
				len--;
			}
			else
			{
				root = node->next;
				if(root)
					root->prev = NULL;
				node->next = node->prev = NULL;
				delete node;
				len--;
			}
			break;
		}
		node = node->next;
	}
}

void drop()
{
	if(len==0)
		return;
	t_node *node = root;
	while(node) 
	{
		root=root->next;
		delete node;
		node = root;
		len--;
	}
} 

unsigned long long calc(unsigned long long N, unsigned long long K)
{
	insert(1, N, 0, 0);

	unsigned long long j;
	unsigned long long l, lnew;

	for(j = 0; j<K; j++)
	{
		t_node *maxidx = root;
		t_node *node = root;
		while(node)
		{
			if(node->l > maxidx->l)
				maxidx = node;
			node = node->next;
		}

		if(maxidx->l == 1)
		{
			l = lnew = 0;
			erase(maxidx->s);
		}
		else
		{
			unsigned long long s = maxidx->s;
			l = maxidx->l/2;
			unsigned long long snew = maxidx->s + l +1;
			lnew = maxidx->l - l - 1;
			if((lnew==0) || (snew>s + maxidx->l -1))
			{
				lnew = snew = 0;
			}

			insert(s, l, snew, lnew);
		}

/*		{
			t_node *node = root;
			cout << endl << j << " --- ";
			while(node)
			{
				cout << node->s << ":" << node->l << ", ";
				node = node->next;
			}
			cout << endl;
		}*/
	}

	cout << max(l, lnew) << " " << min(l, lnew) << endl;

	drop();

	return 0;
}

int main(int argc, char* argv[])
{
	string line;
	getline(cin, line);

	istringstream ss(line);

	int T;
	ss >> T;

	for(int i=0; i<T; i++)
	{
		getline(cin, line);
		istringstream iss(line);

		unsigned long long N, K;
		iss >> N;
		iss >> K;

		cout << "Case #" << i+1 << ": ";

		calc(N, K);
	}


	return 0;
}

