# include <string>
# include <fstream>
# include <utility>

class Solution
{
	public:
		enum Tokens {
			INVALID	= 0,

			NEWLINE	= 12,
			A		= 'a',
			X 		= 'x',
			PLUS	= '+',
			MINUS	= '-',

			NUMBER 	= 512,

			//End

			LAST
		};

		typedef std::pair<Tokens, std::string> Token;

		Solution();
		~Solution() {}

		bool loadFile(std::string& path);
		bool prepFile(std::string& path);
		void solve();

	protected:
		bool			expect(Tokens token);
		bool			getToken();
		long unsigned	strToInt(const std::string& str) const;

		void			writeCase(unsigned caseNum);

		//Overload these
		virtual void	readCase();
		virtual void	doCase();
		virtual void	cleanup();

		//DATA
		std::ifstream	_inputFile;
		std::ofstream	_outputFile;
		unsigned		_numTestCases;
		Token 			_currentToken;
		std::string		_content;
};
