if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/otobit-sahil/moviebot.git
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Movies7x
fi
cd /moviebot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
